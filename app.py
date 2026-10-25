"""AI CareerSpark - run with:  streamlit run app.py

All analysis is rule-based Python (see careerspark/analyzer.py). No live AI model is called.
"""
from html import escape

import streamlit as st

from careerspark import analyzer as an
from careerspark import samples
from careerspark.styles import CSS, HIDE_SIDEBAR

st.set_page_config(page_title="AI CareerSpark", page_icon="✨", layout="wide", initial_sidebar_state="auto")

ICONS = {
    "spark": '<path d="M12 3l1.9 5.1L19 10l-5.1 1.9L12 17l-1.9-5.1L5 10l5.1-1.9z"/><path d="M19 17v4M17 19h4"/>',
    "search": '<circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/>',
    "target": '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/>',
    "chat": '<path d="M21 15a2 2 0 0 1-2 2H8l-5 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
    "pen": '<path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4z"/>',
}

PAGES = [
    ("welcome", "Welcome", ":material/home:"),
    ("dashboard", "Dashboard", ":material/dashboard:"),
    ("analyzer", "Job Description Analyzer", ":material/search:"),
    ("matcher", "Resume and Skills Matcher", ":material/compare_arrows:"),
    ("interview", "Interview Preparation", ":material/forum:"),
    ("improve", "Resume Improvement", ":material/edit_note:"),
    ("about", "About and Help", ":material/help:"),
]
SHARED_KEYS = ["jd_text", "resume_text", "role_title", "improve_text", "res_job", "res_match", "res_q", "res_imp"]


# ------------------------------------------------------------------ helpers
def svg(name: str) -> str:
    return f'<svg viewBox="0 0 24 24" aria-hidden="true">{ICONS[name]}</svg>'


def go(page: str):
    st.session_state["page"] = page


def set_texts(**kwargs):
    for k, v in kwargs.items():
        st.session_state[k] = v


def clear_keys(*keys):
    for k in keys:
        st.session_state.pop(k, None)
        if k.endswith("_text") or k == "role_title":
            st.session_state[k] = ""


def sample_and_go(page: str, **texts):
    set_texts(**texts)
    go(page)


def chips(items, cls="blue") -> str:
    if not items:
        return '<span class="chip gray">None</span>'
    return "".join(f'<span class="chip {cls}">{escape(str(i))}</span>' for i in items)


def card(icon: str, title: str, body: str, cls: str = "") -> str:
    return f'<div class="card {cls}"><div class="ico">{svg(icon)}</div><h4>{escape(title)}</h4><p>{escape(body)}</p></div>'


def page_head(title: str, subtitle: str, mode: str):
    st.markdown(f'<div class="page-head"><span class="pill">{escape(mode)}</span><h1>{escape(title)}</h1><p>{escape(subtitle)}</p></div>',
                unsafe_allow_html=True)


def empty_state(text: str):
    st.markdown(f'<div class="empty">{escape(text)}</div>', unsafe_allow_html=True)


def footer():
    st.markdown('<div class="footer">AI CareerSpark · Built as an assessment project with AI-assisted development · '
                'The analysis inside the app is rule-based, not a live AI model</div>', unsafe_allow_html=True)


def bars(grouped: dict):
    if not grouped:
        return
    top = max(len(v) for v in grouped.values())
    rows = "".join(
        f'<div class="bar-row"><span class="name">{escape(c)}</span><span class="bar"><i style="width:{100 * len(v) / top:.0f}%"></i></span>'
        f'<span class="n">{len(v)}</span></div>' for c, v in sorted(grouped.items(), key=lambda kv: -len(kv[1])))
    st.markdown(rows, unsafe_allow_html=True)


def section(title: str):
    st.markdown(f'<div class="section-title">{escape(title)}</div>', unsafe_allow_html=True)


# --------------------------------------------------------------- sidebar
def sidebar():
    with st.sidebar:
        st.markdown(f'<div class="brand"><span class="logo">{svg("spark")}</span>AI CareerSpark</div>', unsafe_allow_html=True)
        for key, label, icon in PAGES:
            st.button(label, key=f"nav_{key}", icon=icon, use_container_width=True,
                      type="primary" if st.session_state["page"] == key else "secondary", on_click=go, args=(key,))
        st.caption("Understand the role. Improve your skills. Prepare with confidence.")


# ---------------------------------------------------------------- pages
def page_welcome():
    st.markdown(HIDE_SIDEBAR, unsafe_allow_html=True)
    st.markdown(f"""
    <div class="hero">
      <div class="brand"><span class="logo">{svg("spark")}</span>AI CareerSpark</div>
      <span class="pill">For fresh graduates, entry-level applicants and career changers</span>
      <h1>Understand the role. Improve your skills. Prepare with confidence.</h1>
      <p>Paste a job description and see what it really asks for. Compare it with your resume, tighten the wording
      of your experience, and practise the questions you are likely to be asked. Everything runs in your browser session
      with free, rule-based analysis, and every result is explained.</p>
    </div>""", unsafe_allow_html=True)
    st.button("Get Started", type="primary", on_click=go, args=("dashboard",), key="get_started")
    section("What you can do")
    st.markdown('<div class="grid">' + card("search", "Analyze a job description", "Find the skills, responsibilities and experience a posting asks for.")
                + card("target", "Match your resume", "See which job skills appear in your resume and which do not, with an explainable score.")
                + card("chat", "Practise interviews", "Get technical, HR and scenario questions with beginner-friendly sample answers.")
                + card("pen", "Improve your wording", "Get clearer phrasing and suggestions without invented achievements.") + "</div>",
                unsafe_allow_html=True)
    footer()


def page_dashboard():
    page_head("Welcome to AI CareerSpark", "Pick a tool below. A good first step is to paste a job description you are interested in.", "Dashboard")
    cards = [("search", "Job Description Analyzer", "Understand what a role requires.", "analyzer"),
             ("target", "Resume and Skills Matcher", "Compare your resume with a job.", "matcher"),
             ("chat", "Interview Preparation", "Practise likely questions.", "interview"),
             ("pen", "Resume Improvement", "Polish your wording.", "improve")]
    cols = st.columns(4)
    for col, (icon, title, desc, page) in zip(cols, cards):
        with col:
            st.markdown(card(icon, title, desc, "fixed"), unsafe_allow_html=True)
            st.button("Open", key=f"open_{page}", on_click=go, args=(page,), use_container_width=True)
    section("Quick actions")
    q1, q2, q3 = st.columns(3)
    q1.button("Try a sample job description", on_click=sample_and_go, args=("analyzer",), kwargs={"jd_text": samples.SAMPLE_JD},
              use_container_width=True, key="qa1")
    q2.button("Try a sample resume match", on_click=sample_and_go, args=("matcher",),
              kwargs={"jd_text": samples.SAMPLE_JD, "resume_text": samples.SAMPLE_RESUME}, use_container_width=True, key="qa2")
    q3.button("Read how scores work", on_click=go, args=("about",), use_container_width=True, key="qa3")
    section("How to use it")
    st.markdown("""<ol class="steps">
      <li><b>Paste a job description</b> into the Job Description Analyzer to see skills, duties and keywords.</li>
      <li><b>Paste your resume text</b> into the Matcher. The job description you pasted before is kept for the session.</li>
      <li><b>Practise</b> with the Interview Preparation page, using the same job description or just a job title.</li>
      <li><b>Improve</b> a summary or project description, then review every suggestion before you use it.</li>
    </ol>""", unsafe_allow_html=True)
    st.markdown('<div class="notice">New here? Click <b>Try a sample job description</b>. No account or sign-up is needed.</div>', unsafe_allow_html=True)
    footer()


def page_analyzer():
    page_head("Job Description Analyzer", "Paste a job description to see the skills, responsibilities and experience it asks for.",
              "Rule-based analysis")
    st.text_area("Job description", key="jd_text", height=260, placeholder="Paste the full job posting here (at least 25 words)…")
    b1, b2, b3, _ = st.columns([1.2, 1.2, 1, 3])
    run = b1.button("Analyze job", type="primary", key="run_job")
    b2.button("Load sample", on_click=set_texts, kwargs={"jd_text": samples.SAMPLE_JD}, key="sample_job")
    b3.button("Clear", on_click=clear_keys, args=("jd_text", "res_job"), key="clear_job")
    if run:
        ok, msg, text = an.validate_text(st.session_state.get("jd_text", ""), "job description", an.MIN_JD_WORDS)
        if not ok:
            st.session_state.pop("res_job", None)
            st.error(msg)
        else:
            st.session_state["res_job"] = an.analyze_job(text)
            st.success("Analysis complete. Scroll down to see the results.")
            if msg:
                st.warning(msg)
    res = st.session_state.get("res_job")
    if not res:
        empty_state("No results yet. Paste a job description and click Analyze job, or load the sample.")
        return
    if not res["skills"]:
        st.warning("No skills from the built-in list were found. This can happen with very short or unusual descriptions. "
                   "Try pasting the full requirements section.")
    st.markdown(f'<div class="card"><h4>Role summary</h4><p>{escape(res["summary"])}</p></div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        section("Required skills identified")
        for cat, skills in res["grouped"].items():
            st.markdown(f"**{escape(cat)}**<br>{chips(skills)}", unsafe_allow_html=True)
        if not res["skills"]:
            empty_state("No recognised skills.")
        section("Skills by area")
        bars(res["grouped"])
    with c2:
        section("Responsibilities")
        if res["responsibilities"]:
            st.markdown("\n".join(f"- {r}" for r in res["responsibilities"]))
        else:
            st.info("No clear responsibilities section or action-based lines were found.")
        section("Experience and education mentioned")
        if res["experience"]:
            st.markdown("\n".join(f"- {e}" for e in res["experience"]))
        else:
            st.info("No experience requirement was mentioned.")
    section("Important keywords")
    st.markdown("".join(f'<span class="chip violet">{escape(w)} · {n}</span>' for w, n in res["keywords"]) or chips([]), unsafe_allow_html=True)
    section("Suggested preparation areas")
    st.markdown("\n".join(f"- {p}" for p in res["preparation"]))
    st.download_button("Download results (.txt)", an.report_job(res), "job_analysis.txt", "text/plain", key="dl_job")
    st.button("Match my resume to this job", on_click=go, args=("matcher",), key="job_to_match")


def page_matcher():
    page_head("Resume and Skills Matcher", "Compare the skills in your resume with the skills a job description asks for.", "Rule-based analysis")
    c1, c2 = st.columns(2)
    c1.text_area("Your resume text", key="resume_text", height=280, placeholder="Paste your resume text here (at least 20 words)…")
    c2.text_area("Target job description", key="jd_text", height=280, placeholder="Paste the job description here (at least 25 words)…")
    b1, b2, b3, _ = st.columns([1.2, 1.2, 1, 3])
    run = b1.button("Compare skills", type="primary", key="run_match")
    b2.button("Load sample", on_click=set_texts, kwargs={"jd_text": samples.SAMPLE_JD, "resume_text": samples.SAMPLE_RESUME}, key="sample_match")
    b3.button("Clear", on_click=clear_keys, args=("resume_text", "jd_text", "res_match"), key="clear_match")
    if run:
        ok1, m1, resume = an.validate_text(st.session_state.get("resume_text", ""), "resume text", an.MIN_RESUME_WORDS)
        ok2, m2, jd = an.validate_text(st.session_state.get("jd_text", ""), "job description", an.MIN_JD_WORDS)
        if not ok1:
            st.error(m1)
        if not ok2:
            st.error(m2)
        if ok1 and ok2:
            result = an.match_resume(resume, jd)
            if not result["jd_skills"]:
                st.session_state.pop("res_match", None)
                st.error("No recognisable skills were found in the job description, so a score cannot be calculated. "
                         "Paste the section that lists requirements or skills.")
            else:
                st.session_state["res_match"] = result
                st.success("Comparison complete.")
                for m in (m1, m2):
                    if m:
                        st.warning(m)
        else:
            st.session_state.pop("res_match", None)
    res = st.session_state.get("res_match")
    if not res:
        empty_state("No results yet. Add your resume and a job description, then click Compare skills.")
        return
    left, right = st.columns([1, 2])
    with left:
        st.markdown(f'<div class="card"><div class="ring" style="--p:{res["score"]}"><div class="ring-in"><b>{res["score"]:g}%</b>'
                    f'<span>{escape(res["band"])}</span></div></div></div>', unsafe_allow_html=True)
    with right:
        st.markdown(f'<div class="card"><h4>How this score was calculated</h4><p>Score = job skills also found in your resume ÷ skills found in the '
                    f'job description × 100.<br><b>{escape(res["formula"])}</b></p></div>', unsafe_allow_html=True)
        st.markdown('<div class="notice">This is a text-based estimate, not a prediction of hiring success. It can miss skills you describe in '
                    'different words and cannot judge quality or depth of experience.</div>', unsafe_allow_html=True)
    section("Skills found in your resume")
    st.markdown(chips(res["resume_skills"], "blue"), unsafe_allow_html=True)
    section("Skills mentioned in the job description")
    st.markdown(chips(res["jd_skills"], "violet"), unsafe_allow_html=True)
    m1, m2 = st.columns(2)
    with m1:
        section(f"Matching skills ({len(res['matched'])})")
        st.markdown(chips(res["matched"], "good"), unsafe_allow_html=True)
    with m2:
        section(f"Not identified in your resume ({len(res['missing'])})")
        st.markdown(chips(res["missing"], "warn"), unsafe_allow_html=True)
    section("Suggested areas for improvement")
    if res["tips"]:
        st.markdown("\n".join(f"- {t}" for t in res["tips"]))
    else:
        st.success("Every skill found in the job description also appears in your resume text.")
    if res["extra"]:
        section("Other skills in your resume (not mentioned in this job description)")
        st.markdown(chips(res["extra"], "gray"), unsafe_allow_html=True)
    st.download_button("Download results (.txt)", an.report_match(res), "resume_match.txt", "text/plain", key="dl_match")


def page_interview():
    page_head("Interview Preparation", "Enter a job title, paste a job description, or both, to get practice questions.",
              "Rule-based templates, not live AI")
    st.text_input("Job title (optional if you paste a job description)", key="role_title", placeholder="For example: Junior Data Analyst")
    st.text_area("Job description (optional)", key="jd_text", height=200, placeholder="Paste a job description for more relevant questions…")
    b1, b2, b3, _ = st.columns([1.3, 1.2, 1, 3])
    run = b1.button("Generate questions", type="primary", key="run_q")
    b2.button("Load sample", on_click=set_texts, kwargs={"jd_text": samples.SAMPLE_JD, "role_title": "Junior Data Analyst"}, key="sample_q")
    b3.button("Clear", on_click=clear_keys, args=("role_title", "jd_text", "res_q"), key="clear_q")
    if run:
        title = st.session_state.get("role_title", "").strip()
        jd_raw = st.session_state.get("jd_text", "").strip()
        jd = ""
        if not title and not jd_raw:
            st.session_state.pop("res_q", None)
            st.error("Please enter a job title or paste a job description.")
        else:
            if jd_raw:
                ok, msg, jd = an.validate_text(jd_raw, "job description", an.MIN_JD_WORDS)
                if not ok and not title:
                    st.session_state.pop("res_q", None)
                    st.error(msg + " Alternatively, enter a job title.")
                    jd = None
                elif not ok:
                    st.warning(msg + " Questions will be based on the job title instead.")
                    jd = ""
            if jd is not None:
                st.session_state["res_q"] = an.generate_questions(title, jd)
                st.success("Questions generated.")
    res = st.session_state.get("res_q")
    if not res:
        empty_state("No questions yet. Enter a job title or paste a job description, then click Generate questions.")
        return
    if res["source"] == "none":
        st.warning("No known skills were found, so only general HR and scenario questions are shown. "
                   "Try a more specific title (such as 'Data Analyst') or paste a job description.")
    else:
        st.info(f"Technical questions are based on the {res['source']}: {', '.join(res['skills'][:10])}.")
    st.markdown('<div class="notice">All questions and sample answers come from built-in templates written for this app (rule-based). '
                'They are examples to learn from. Use your own real experience in your answers.</div>', unsafe_allow_html=True)
    tabs = st.tabs([f"Technical ({len(res['technical'])})", f"HR ({len(res['hr'])})", f"Scenario ({len(res['scenario'])})"])
    for tab, name in zip(tabs, ("technical", "hr", "scenario")):
        with tab:
            if not res[name]:
                empty_state("No questions in this group for the information provided.")
            for i, item in enumerate(res[name], 1):
                with st.expander(f"{i}. {item['question']}"):
                    st.markdown(f'<span class="diff {item["difficulty"]}">{item["difficulty"]}</span>'
                                f'<span class="chip gray">Rule-based template</span>', unsafe_allow_html=True)
                    st.markdown(f"**Sample answer (beginner-friendly):** {item['answer']}")
                    st.markdown(f"**Preparation tip:** {item['tip']}")
    st.download_button("Download questions (.txt)", an.report_questions(res), "interview_practice.txt", "text/plain", key="dl_q")


def page_improve():
    page_head("Resume Improvement", "Paste a summary, experience or project description to get clearer wording and suggestions.",
              "Rule-based rewriting")
    st.text_area("Text to improve", key="improve_text", height=180, placeholder="Paste a resume summary, experience or project description…")
    with st.expander("Target job description (optional, for relevant keywords)"):
        st.text_area("Job description", key="jd_text", height=160, label_visibility="collapsed")
    b1, b2, b3, _ = st.columns([1.2, 1.2, 1, 3])
    run = b1.button("Improve wording", type="primary", key="run_imp")
    b2.button("Load sample", on_click=set_texts, kwargs={"improve_text": samples.SAMPLE_IMPROVE, "jd_text": samples.SAMPLE_JD}, key="sample_imp")
    b3.button("Clear", on_click=clear_keys, args=("improve_text", "jd_text", "res_imp"), key="clear_imp")
    if run:
        ok, msg, text = an.validate_text(st.session_state.get("improve_text", ""), "text", an.MIN_IMPROVE_WORDS)
        if not ok:
            st.session_state.pop("res_imp", None)
            st.error(msg)
        else:
            st.session_state["res_imp"] = an.improve_text(text, st.session_state.get("jd_text", ""))
            st.success("Suggestions ready. Please review them before using them.")
            if msg:
                st.warning(msg)
    res = st.session_state.get("res_imp")
    if not res:
        empty_state("No results yet. Paste some text and click Improve wording, or load the sample.")
        return
    st.markdown('<div class="notice">The tool only rewords what you wrote. It never adds qualifications, jobs, achievements or numbers. '
                'Check that every line is still true before you use it.</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        section("Original text")
        st.code(res["original"], language=None, wrap_lines=True)
    with c2:
        section("Improved wording (use the copy icon in the box)")
        st.code(res["improved"], language=None, wrap_lines=True)
    section("Suggestions for clarity and relevance")
    st.markdown("\n".join(f"- {s}" for s in res["suggestions"]))
    if res["changes"]:
        with st.expander(f"See the {len(res['changes'])} wording change(s)"):
            st.markdown("\n".join(f"- {c}" for c in res["changes"]))
    section("Relevant keywords from the job description")
    if res["jd_keywords"]:
        st.markdown("Include these **only if they are true for you**:", unsafe_allow_html=True)
        st.markdown(chips(res["keywords_to_consider"] or res["jd_keywords"], "violet"), unsafe_allow_html=True)
    else:
        st.info("Add a target job description (above) to see relevant keywords.")
    st.download_button("Download results (.txt)", an.report_improve(res), "resume_wording.txt", "text/plain", key="dl_imp")


def page_about():
    page_head("About and Help", "What AI CareerSpark does, how each tool works and what its limits are.", "Help")
    section("What the app does")
    st.write("AI CareerSpark helps job seekers read a job description, compare it with their resume, practise interview questions and "
             "tidy resume wording. It is a prototype built as an assessment project.")
    section("Real AI or rule-based?")
    st.markdown("""
| Part | How it works |
|---|---|
| Building this app | **AI-assisted development.** An AI assistant (Claude) helped plan, write and review the code. |
| Job analysis, matching, questions, wording | **Rule-based Python.** Keyword lists, regular expressions and templates. |
| Live AI model inside the app | **None.** The app does not call any AI service. |
""")
    section("How to use each feature")
    with st.expander("Job Description Analyzer"):
        st.write("Paste a job posting (25 words or more) and click Analyze job. You get a role summary, skills, responsibilities, experience "
                 "mentions, keywords and preparation areas.")
    with st.expander("Resume and Skills Matcher"):
        st.write("Paste your resume text and a job description, then click Compare skills.")
    with st.expander("Interview Preparation"):
        st.write("Enter a job title, a job description or both. Open a question to see a sample answer and a tip.")
    with st.expander("Resume Improvement"):
        st.write("Paste a summary or project description. Review the rewritten version, then copy it with the icon at the top of the box.")
    section("How the match score is calculated")
    st.markdown("""
1. The app searches both texts for skills from a built-in list (about 90 skills with alternative spellings).
2. **Score = (job-description skills also found in the resume) ÷ (skills found in the job description) × 100**, rounded to one decimal place.
3. Labels: 75 and above = strong, 50 to 74 = moderate, 25 to 49 = partial, below 25 = low text overlap.

All skills count equally. The score is **not** a prediction of hiring success.
""")
    section("Limitations")
    st.markdown("""
- Only skills in the built-in list are recognised. Other skills and different wording can be missed.
- Matching is by words, so it cannot judge how well you know a skill.
- Sample answers are generic templates. Personalise them with real experience.
- Responsibilities and titles are guessed from layout and wording, so they can be wrong for unusual formats.
- Text is limited to 15,000 characters per box.
""")
    section("How your information is handled")
    st.write("Text you enter is processed by the app while your session is open and is not written to a file or database by this app's code. "
             "The app has no accounts, encryption or deletion feature. If you use a hosted copy, the hosting provider may keep technical logs "
             "outside this app's control. Please avoid pasting sensitive personal details such as ID numbers, home address or phone number.")
    footer()


PAGE_FUNCS = {"welcome": page_welcome, "dashboard": page_dashboard, "analyzer": page_analyzer, "matcher": page_matcher,
              "interview": page_interview, "improve": page_improve, "about": page_about}


def main():
    st.markdown(CSS, unsafe_allow_html=True)
    st.session_state.setdefault("page", "welcome")
    # Keep shared values alive when the widgets that own them are not on the current page
    for k in SHARED_KEYS:
        if k in st.session_state:
            st.session_state[k] = st.session_state[k]
    if st.session_state["page"] != "welcome":
        sidebar()
    PAGE_FUNCS[st.session_state["page"]]()
    if st.session_state["page"] in ("analyzer", "matcher", "interview", "improve"):
        footer()


main()
