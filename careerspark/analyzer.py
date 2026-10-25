"""Rule-based text analysis for AI CareerSpark.

IMPORTANT: Nothing in this module calls an AI model. It uses keyword lists,
regular expressions and templates. Results depend entirely on the text supplied.
"""
from __future__ import annotations

import re
from collections import Counter

from .skills_data import (
    ACTION_VERBS, GENERIC_JOB_WORDS, HR_QUESTIONS, PREP_BY_CATEGORY, ROLE_PROFILES,
    SCENARIO_TEMPLATES, SKILL_CATEGORY, SKILL_QUESTIONS, SKILLS, STOPWORDS,
)

MAX_CHARS = 15000
MIN_JD_WORDS = 25
MIN_RESUME_WORDS = 20
MIN_IMPROVE_WORDS = 5


# ---------------------------------------------------------------- validation
def validate_text(text: str, label: str, min_words: int) -> tuple[bool, str, str]:
    """Return (ok, message, cleaned_text). Long text is trimmed with a notice."""
    text = (text or "").strip()
    if not text:
        return False, f"Please paste the {label} first.", ""
    letters = sum(c.isalpha() for c in text)
    if letters < 0.4 * len(text.replace(" ", "").replace("\n", "")):
        return False, f"The {label} looks like it contains mostly symbols or numbers. Please paste normal text.", ""
    words = len(text.split())
    if words < min_words:
        return False, (f"The {label} is too short ({words} words). Please provide at least {min_words} words "
                       f"so there is enough information to analyse."), ""
    note = ""
    if len(text) > MAX_CHARS:
        text = text[:MAX_CHARS]
        note = f"The {label} was very long, so only the first {MAX_CHARS:,} characters were analysed."
    return True, note, text


# ------------------------------------------------------------ skill finding
def _build_patterns() -> list[tuple[str, re.Pattern]]:
    patterns = []
    for group in SKILLS.values():
        for skill, aliases in group.items():
            alts = sorted({re.escape(a) for a in aliases}, key=len, reverse=True)
            # Allow simple plurals, and make sure we do not match inside longer words
            regex = r"(?<![A-Za-z0-9+#])(?:" + "|".join(alts) + r")(?:s|es)?(?![A-Za-z0-9+#])"
            patterns.append((skill, re.compile(regex, re.IGNORECASE)))
    return patterns


_PATTERNS = _build_patterns()


def find_skills(text: str) -> list[str]:
    """Return canonical skill names found in text, in order of first appearance."""
    hits = []
    for skill, pattern in _PATTERNS:
        m = pattern.search(text or "")
        if m:
            hits.append((m.start(), skill))
    return [s for _, s in sorted(hits)]


def skill_counts(text: str) -> dict[str, int]:
    return {skill: len(p.findall(text or "")) for skill, p in _PATTERNS if p.search(text or "")}


def group_by_category(skills: list[str]) -> dict[str, list[str]]:
    grouped: dict[str, list[str]] = {}
    for s in skills:
        grouped.setdefault(SKILL_CATEGORY[s], []).append(s)
    return grouped


# ------------------------------------------------------- job description
HEADER_RE = re.compile(r"^\s*(?:[-*•#]+\s*)?([A-Za-z' ’/&]{3,50}?)\s*:?\s*$")
RESP_HEADERS = ("responsibilities", "duties", "what you will do", "what you'll do", "what you’ll do", "your role",
                "key responsibilities", "the role", "day to day", "day-to-day", "you will")
OTHER_HEADERS = ("requirements", "qualifications", "skills", "what we offer", "benefits", "about", "preferred",
                 "nice to have", "who you are", "what you bring", "education", "experience", "how to apply", "we offer")


def _clean_line(line: str) -> str:
    return re.sub(r"^\s*(?:[-*•▪●◦‣·]|\d+[.)])\s*", "", line).strip()


def _guess_title(text: str) -> str:
    for pat in (r"(?im)^\s*(?:job\s+title|position|role|title)\s*[:\-]\s*(.{3,70})$",):
        m = re.search(pat, text)
        if m:
            return m.group(1).strip().rstrip(".")
    first = next((l.strip() for l in text.splitlines() if l.strip()), "")
    if first and len(first.split()) <= 9 and not first.endswith((".", ",")) and not first.lower().startswith(("we ", "about")):
        return first.strip(" -:")
    m = re.search(r"(?i)(?:hiring|looking for|seeking|recruiting)\s+(?:an?|the)?\s*([A-Za-z][A-Za-z /&-]{3,45}?)(?:\s+to\b|\s+who\b|\s+with\b|[.,;]|$)", text)
    if m:
        return m.group(1).strip()
    return "Not clearly stated"


def _extract_responsibilities(text: str) -> list[str]:
    lines = text.splitlines()
    out, in_section = [], False
    for line in lines:
        stripped = line.strip()
        low = stripped.lower().rstrip(":")
        if not stripped:
            continue
        is_header = bool(HEADER_RE.match(stripped)) and len(stripped.split()) <= 6 and not stripped.endswith(".")
        if is_header and any(low.startswith(h) for h in RESP_HEADERS):
            in_section = True
            continue
        if is_header and any(low.startswith(h) for h in OTHER_HEADERS):
            in_section = False
            continue
        if in_section:
            out.append(_clean_line(stripped))
    if not out:  # fallback: sentences/bullets that start with an action verb
        for line in lines:
            c = _clean_line(line)
            first = re.sub(r"[^a-z]", "", c.split()[0].lower()) if c.split() else ""
            if c and (first in ACTION_VERBS or re.sub(r"(s|es)$", "", first) in ACTION_VERBS) and len(c.split()) >= 4:
                out.append(c)
    return [o.rstrip(".;") for o in out if len(o.split()) >= 3][:10]


def _extract_experience(text: str) -> list[str]:
    found = []
    for sentence in re.split(r"(?<=[.!?])\s+|\n+", text):
        s = sentence.strip()
        if not s:
            continue
        low = s.lower()
        if (re.search(r"\b\d+\s*(?:\+|-\s*\d+|to\s*\d+)?\s*(?:years?|yrs?)\b", low)
                or re.search(r"\b(entry[- ]level|fresher|freshers|graduate|junior|intern(?:ship)?|senior|mid[- ]level|no experience|bachelor|master'?s|degree|diploma|b\.?tech|b\.?sc|certification)\b", low)):
            found.append(_clean_line(s)[:220])
    return found[:6]


def _seniority(text: str) -> str:
    low = text.lower()
    if re.search(r"\b(senior|lead|principal|manager|\d{1,2}\s*\+?\s*years)\b", low):
        m = re.search(r"\b(\d{1,2})\s*\+?\s*years", low)
        if m and int(m.group(1)) <= 2:
            return "entry-level"
        if re.search(r"\b(senior|lead|principal|manager)\b", low) or (m and int(m.group(1)) >= 5):
            return "senior"
        return "mid-level"
    if re.search(r"\b(entry[- ]level|fresher|freshers|graduate|junior|intern|trainee|associate|no experience)\b", low):
        return "entry-level"
    return "unspecified level"


def top_keywords(text: str, limit: int = 15) -> list[tuple[str, int]]:
    words = re.findall(r"[A-Za-z][A-Za-z+#.\-]{2,}", text.lower())
    words = [w.strip(".-") for w in words]
    counts = Counter(w for w in words if len(w) > 3 and w not in STOPWORDS and w not in GENERIC_JOB_WORDS)
    return counts.most_common(limit)


def analyze_job(text: str) -> dict:
    """Analyse a (validated) job description."""
    skills = find_skills(text)
    grouped = group_by_category(skills)
    title = _guess_title(text)
    level = _seniority(text)
    main_cats = sorted(grouped, key=lambda c: -len(grouped[c]))[:3]
    if skills:
        focus = ", ".join(c.lower() for c in main_cats)
        article = "an" if level[0] in "aeiou" else "a"
        summary = (f"This looks like {article} {level} role{'' if title == 'Not clearly stated' else ' (' + title + ')'} "
                   f"with a focus on {focus}. The text mentions {len(skills)} recognisable skills.")
    else:
        summary = ("The text does not mention skills from the built-in skill list, so a detailed summary is not possible. "
                   "Try pasting the full requirements section.")
    prep = [f"{cat}: {PREP_BY_CATEGORY[cat]} (skills: {', '.join(grouped[cat])})" for cat in main_cats]
    if not prep:
        prep = ["Review the responsibilities listed and prepare one real example for each."]
    return {
        "title": title, "level": level, "summary": summary, "skills": skills, "grouped": grouped,
        "responsibilities": _extract_responsibilities(text), "experience": _extract_experience(text),
        "keywords": top_keywords(text), "preparation": prep, "word_count": len(text.split()),
    }


# ---------------------------------------------------------------- matching
def band(score: float) -> str:
    if score >= 75:
        return "Strong text overlap"
    if score >= 50:
        return "Moderate text overlap"
    if score >= 25:
        return "Partial text overlap"
    return "Low text overlap"


def match_resume(resume: str, jd: str) -> dict:
    """Score = (job skills also found in resume) / (job skills found) x 100."""
    jd_skills = find_skills(jd)
    resume_skills = find_skills(resume)
    matched = [s for s in jd_skills if s in resume_skills]
    missing = [s for s in jd_skills if s not in resume_skills]
    extra = [s for s in resume_skills if s not in jd_skills]
    score = round(100 * len(matched) / len(jd_skills), 1) if jd_skills else 0.0
    tips = []
    for cat, skills in group_by_category(missing).items():
        tips.append(f"{cat}: {', '.join(skills)} not found. If you have genuinely used these, add them where they apply "
                    f"(skills section, projects or experience). If not, consider learning them. {PREP_BY_CATEGORY[cat]}")
    return {
        "jd_skills": jd_skills, "resume_skills": resume_skills, "matched": matched, "missing": missing,
        "extra": extra, "score": score, "band": band(score), "tips": tips,
        "formula": f"{len(matched)} matched / {len(jd_skills)} job skills x 100 = {score}%",
    }


# --------------------------------------------------------------- interview
def _skills_from_title(title: str) -> list[str]:
    low = (title or "").lower()
    found = list(find_skills(title or ""))
    for key, skills in ROLE_PROFILES.items():
        if re.search(r"\b" + re.escape(key) + r"\b", low):
            found += [s for s in skills if s not in found]
    return found


def generate_questions(title: str = "", jd: str = "") -> dict:
    """Build template-based questions. Every item is labelled as rule-based."""
    jd_skills = find_skills(jd) if jd else []
    skills = jd_skills or _skills_from_title(title)
    source = "job description" if jd_skills else ("job title" if skills else "none")
    technical, scenario = [], []
    generic_answer = ("I would explain what it is in simple words, describe where I have used it (for example in a course, "
                      "project or practice task: add your own real example here), and mention what I am still learning.")
    for s in skills:
        if s in SKILL_QUESTIONS:
            q, a, d = SKILL_QUESTIONS[s]
            technical.append({"skill": s, "question": q, "answer": a, "difficulty": d,
                              "tip": f"Practise explaining {s} aloud with one small example from your own work."})
        elif SKILL_CATEGORY[s] != "Soft Skills":
            technical.append({"skill": s, "question": f"How have you used {s}, and what would you like to learn more about?",
                              "answer": generic_answer, "difficulty": "Beginner",
                              "tip": f"Prepare one honest, specific example involving {s}."})
    cats = list(dict.fromkeys(SKILL_CATEGORY[s] for s in skills))
    for c in cats:
        if c in SCENARIO_TEMPLATES:
            q, a, d = SCENARIO_TEMPLATES[c]
            scenario.append({"skill": c, "question": q, "answer": a, "difficulty": d,
                             "tip": "Describe your thinking step by step and say who you would involve."})
    if "Soft Skills" not in cats:
        q, a, d = SCENARIO_TEMPLATES["Soft Skills"]
        scenario.append({"skill": "Soft Skills", "question": q, "answer": a, "difficulty": d,
                         "tip": "Describe your thinking step by step and say who you would involve."})
    hr = [{"skill": "HR", "question": q, "difficulty": d, "answer": a, "tip": t} for q, d, a, t in HR_QUESTIONS]
    return {"source": source, "skills": skills, "technical": technical[:10], "hr": hr, "scenario": scenario[:5]}


# ---------------------------------------------------------- resume wording
GERUND_TO_PAST = {
    "managing": "Managed", "developing": "Developed", "creating": "Created", "building": "Built", "designing": "Designed",
    "testing": "Tested", "analyzing": "Analyzed", "analysing": "Analysed", "handling": "Handled", "leading": "Led",
    "maintaining": "Maintained", "preparing": "Prepared", "organizing": "Organized", "organising": "Organised",
    "coordinating": "Coordinated", "writing": "Wrote", "implementing": "Implemented", "supporting": "Supported",
    "monitoring": "Monitored", "training": "Trained", "presenting": "Presented", "researching": "Researched",
    "planning": "Planned", "reviewing": "Reviewed", "assisting": "Assisted", "cleaning": "Cleaned", "updating": "Updated",
    "documenting": "Documented", "recording": "Recorded", "answering": "Answered", "scheduling": "Scheduled",
}
VERB_PAST = {"develop": "Developed", "build": "Built", "create": "Created", "design": "Designed", "manage": "Managed",
             "handle": "Handled", "write": "Wrote", "test": "Tested", "analyze": "Analyzed", "prepare": "Prepared",
             "maintain": "Maintained", "lead": "Led", "support": "Supported", "assist": "Assisted", "organize": "Organized"}
WEAK_PHRASES = [
    (r"\bworked on\b", "contributed to"), (r"\bhelped with\b", "assisted with"),
    (r"\bwas part of a team that\b", "contributed to a team that"), (r"\bin charge of\b", "oversaw"),
    (r"\bwas involved in\b", "participated in"), (r"\bduties included\b", "handled"),
    (r"\bresponsible for\b", "handled"),
]
IRREGULAR_PAST = {"built", "led", "wrote", "ran", "made", "taught", "kept", "sold", "won", "drew", "held", "met", "began", "found"}
FILLER = ["very", "really", "basically", "actually", "quite", "just"]
CLICHES = ["hard-working", "hard working", "team player", "go-getter", "self-motivated", "detail-oriented", "passionate",
           "dynamic", "results-driven", "think outside the box", "responsible for", "various", "a lot of"]


def _rewrite_sentence(s: str, changes: list[str]) -> str:
    original = s
    s = s.strip()
    if not s:
        return s
    # "I am/was responsible for managing X" -> "Managed X"
    m = re.match(r"(?i)^(?:i\s+(?:am|was)\s+|my\s+(?:role|duty|job)\s+(?:is|was)\s+(?:to\s+)?)?(?:responsible for|in charge of|tasked with)\s+(\w+ing)\b(.*)$", s)
    if m and m.group(1).lower() in GERUND_TO_PAST:
        s = GERUND_TO_PAST[m.group(1).lower()] + m.group(2)
    # Only drop a leading "I" when the next word is a past-tense verb; otherwise keep the sentence as written.
    words = s.split()
    if words and words[0].lower() in ("i", "i've"):
        nxt = words[1].lower() if len(words) > 1 else ""
        if nxt.endswith("ed") or nxt in IRREGULAR_PAST:
            s = " ".join(words[1:])
        else:
            return s[0].upper() + s[1:]
    s = re.sub(r"\band I (?=\w+ed\b)", "and ", s)
    for pat, rep in WEAK_PHRASES:
        s = re.sub(pat, rep, s, flags=re.IGNORECASE)
    for f in FILLER:
        s = re.sub(r"\b" + f + r"\s+", "", s, flags=re.IGNORECASE)
    s = re.sub(r"\bmy\s+(team|project|work)\b", r"the \1", s, flags=re.IGNORECASE)
    s = re.sub(r"\s{2,}", " ", s).strip(" ,")
    first = s.split()[0].lower() if s.split() else ""
    if first in VERB_PAST:
        s = VERB_PAST[first] + s[len(first):]
    if s:
        s = s[0].upper() + s[1:]
    if s != original.strip():
        changes.append(f"“{original.strip()}” → “{s}”")
    return s


def improve_text(text: str, jd: str = "") -> dict:
    """Rewrite wording using simple rules. Never adds new facts."""
    text = text.strip()
    pieces = [p for p in re.split(r"(?<=[.!?])\s+|\n+", text) if p.strip()]
    pieces = [_clean_line(p) for p in pieces]
    changes: list[str] = []
    rewritten = [_rewrite_sentence(p.rstrip(".!"), changes) for p in pieces]
    rewritten = [r for r in rewritten if r]
    improved = "\n".join("- " + r.rstrip(".") + "." for r in rewritten) if len(rewritten) > 1 else (rewritten[0].rstrip(".") + "." if rewritten else "")

    low = text.lower()
    suggestions = []
    if not re.search(r"\d", text):
        suggestions.append("No numbers were found. If you have real figures (for example number of users, files, patients, "
                           "hours saved or marks), add them. Do not estimate or invent numbers.")
    first_words = {p.split()[0].lower() for p in pieces if p.split()}
    if not first_words & (set(VERB_PAST) | {v + "d" for v in ACTION_VERBS} | {v + "ed" for v in ACTION_VERBS} | {w.lower() for w in GERUND_TO_PAST.values()}):
        suggestions.append("Start each point with a strong action verb such as Built, Analysed, Prepared or Coordinated.")
    if re.search(r"\b(i|my|me)\b", low):
        suggestions.append("Avoid first-person words (I, my). Resume bullets normally start directly with the action.")
    found_cliches = [c for c in CLICHES if c in low]
    if found_cliches:
        suggestions.append("These phrases are vague or overused: " + ", ".join(found_cliches) +
                           ". Replace them with a specific example of what you did.")
    long_sentences = [p for p in pieces if len(p.split()) > 30]
    if long_sentences:
        suggestions.append(f"{len(long_sentences)} sentence(s) are longer than 30 words. Split them into shorter points.")
    if len(text.split()) < 15:
        suggestions.append("This text is short. Add what you did, which tools you used and what the outcome was, using true details only.")
    suggestions.append("Tell the reader what the result or benefit was, if you know it. State only facts you can verify.")

    keywords_to_consider, jd_skills = [], []
    if jd.strip():
        jd_skills = find_skills(jd)
        present = set(find_skills(text))
        keywords_to_consider = [s for s in jd_skills if s not in present]
    return {"original": text, "improved": improved, "changes": changes, "suggestions": suggestions,
            "jd_keywords": jd_skills, "keywords_to_consider": keywords_to_consider}


# ------------------------------------------------------------------ reports
def report_job(a: dict) -> str:
    lines = ["AI CareerSpark - Job Description Analysis (rule-based)", "", f"Role: {a['title']}", f"Level: {a['level']}",
             "", a["summary"], "", "Skills identified:"]
    lines += [f"- {s}" for s in a["skills"]] or ["- none"]
    lines += ["", "Responsibilities:"] + ([f"- {r}" for r in a["responsibilities"]] or ["- none found"])
    lines += ["", "Experience / education mentioned:"] + ([f"- {e}" for e in a["experience"]] or ["- none found"])
    lines += ["", "Keywords: " + ", ".join(f"{w} ({n})" for w, n in a["keywords"]), "", "Preparation areas:"]
    lines += [f"- {p}" for p in a["preparation"]]
    return "\n".join(lines)


def report_match(m: dict) -> str:
    lines = ["AI CareerSpark - Resume and Skills Match (rule-based estimate, not a hiring prediction)", "",
             f"Score: {m['score']}%  ({m['band']})", f"Calculation: {m['formula']}", "",
             "Matching skills: " + (", ".join(m["matched"]) or "none"),
             "Not identified in resume: " + (", ".join(m["missing"]) or "none"),
             "Other skills in resume: " + (", ".join(m["extra"]) or "none"), "", "Suggestions:"]
    lines += [f"- {t}" for t in m["tips"]] or ["- All job skills found in the resume text."]
    return "\n".join(lines)


def report_questions(q: dict) -> str:
    lines = ["AI CareerSpark - Interview Practice (rule-based templates, not live AI)", ""]
    for name in ("technical", "hr", "scenario"):
        lines += [name.upper(), ""]
        for i, item in enumerate(q[name], 1):
            lines += [f"{i}. [{item['difficulty']}] {item['question']}", f"   Sample answer: {item['answer']}",
                      f"   Tip: {item['tip']}", ""]
    return "\n".join(lines)


def report_improve(r: dict) -> str:
    lines = ["AI CareerSpark - Resume Wording (rule-based)", "", "ORIGINAL", r["original"], "", "IMPROVED", r["improved"],
             "", "SUGGESTIONS"] + [f"- {s}" for s in r["suggestions"]]
    if r["keywords_to_consider"]:
        lines += ["", "Keywords from the job description to include ONLY if true for you: " + ", ".join(r["keywords_to_consider"])]
    return "\n".join(lines)
