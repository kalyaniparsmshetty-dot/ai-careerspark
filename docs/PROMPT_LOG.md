# Prompt Documentation: AI CareerSpark

> **How to use this file truthfully.** Sections marked **SUGGESTED** are ideas you can reuse. They are *not* a record of what was done.
> Sections marked **ACTUAL** are for prompts you really sent. Copy them from your chat history, and delete anything you did not use.
> Do not copy suggested prompts into the "actual" log unless you really sent them.

## 1. Project objective
Build a free, working web application, AI CareerSpark, that helps job seekers analyse job descriptions, compare resume skills, practise interviews and improve resume wording. Constraints: free tools only, no paid APIs, beginner-friendly, complete working files.

## 2. AI tools used
| Tool | Used for | Evidence you can attach |
|---|---|---|
| Claude (Anthropic) | Architecture, code, UI, tests, documentation | Chat link or screenshots |
| ChatGPT (optional) | Add this row only if you really used it | Chat link or screenshots |

**Where AI is and is not used**
- AI-assisted development: yes (Claude helped write and review the code).
- Live AI inside the finished app: **no**. The features are rule-based Python.

## 3. ACTUAL prompts (fill in as you work)

### Prompt 1: Initial project prompt (ACTUAL: already sent)
- **Prompt:** The full "PROJECT DEVELOPMENT PROMPT: AI CAREERSPARK" you pasted (14 numbered sections covering requirements, stack, UI, features, AI honesty, testing, setup and deliverables). Paste it here in full.
- **Intended outcome:** A complete working project, documentation and scripts.
- **Result received:** *(describe what you actually received, e.g. "a Streamlit app with 7 pages, tests, and docs")*
- **Problems you noticed:** *(write only what you noticed)*
- **Follow-up prompt:** *(paste)*
- **Improvement made:** *(describe)*
- **Actual test result:** *(describe what you saw when you ran it)*

### Prompt 2 to N: copy this block for each new prompt
```
Date/time:
Prompt (paste exactly):
Intended outcome:
Result received:
Problems identified:
Follow-up prompt used:
Improvement made:
Actual test result on my computer:
```

## 4. SUGGESTED prompts (not yet used; label them as used only if you send them)

**Architecture.** "Propose the simplest free architecture for a Python/Streamlit career assistant with 7 pages, no database and no paid API. List files and the purpose of each, and explain the trade-offs of rule-based analysis versus a live AI model."

**Interface design.** "Design a clean SaaS-style Streamlit interface: navy text, light-blue background, blue-to-violet accents, rounded cards, a sidebar and a hero welcome page. Give the CSS and explain how it works on mobile."

**Feature: resume matcher.** "Write a matcher that extracts skills from a resume and a job description, lists matching and missing skills, and calculates a score. The score must come from a documented formula and must change with the input."

**Feature: interview questions.** "Generate technical, HR and scenario questions from the skills in a job description, with beginner-friendly sample answers and difficulty labels. Label them as template-based."

**Feature: resume wording.** "Rewrite resume bullets with stronger verbs. Never add facts, numbers, employers or skills the user did not write."

**Debugging.** "Here is the error message and the code: [paste]. Explain the cause in simple words and give the corrected full file."

**Edge cases.** "List edge cases for a text-analysis app (empty input, very short input, very long input, symbols only, non-English text) and write tests for each."

**Testing.** "Write pytest tests proving that different resumes give different scores and that the score equals matched divided by job skills times 100."

**Documentation.** "Write a beginner-friendly README and a 2-minute video script. Do not claim anything that has not been tested."

## 5. Worked example of iterative prompt improvement (ILLUSTRATION: written as an example, not a claim of history)

| Step | Prompt | Likely weakness | Refinement |
|---|---|---|---|
| v1 | "Make a resume matcher." | Vague. May return a hardcoded demo score, no validation, no explanation. | Add requirements. |
| v2 | "Make a resume matcher in Streamlit that compares resume text with a job description." | Better, but the score formula is unspecified and the tool may sound like a hiring predictor. | Specify the formula and honesty rules. |
| v3 | "Build a Streamlit matcher. Extract skills from both texts using a documented list. Score = matched job skills / job skills x 100. Show matching, missing and extra skills. Validate empty, short and symbol-only input with clear messages. State that the score is an estimate, not a hiring prediction. No hardcoded results. Add tests proving the score changes with different resumes." | Complete and testable. | Use this style: goal, inputs, formula, validation, honesty, tests. |

The finished app follows the v3 style. If you sent different prompts, replace this table with your real versions.

## 6. Debugging and refinement log
Items below were observed **by the AI while building and testing** this project in one session. Include one only if you have reviewed it and it is true to say it happened in your project.
1. Job summary read "a entry-level role". Fixed by choosing "a" or "an" from the first letter.
2. Resume rewriter left "and I assisted" and produced "Am a hard working team player…" from "I am a hard working team player". Fixed so a leading "I" is removed only before a past-tense action verb; other sentences are kept as written.
3. Sidebar styling did not appear after an edit until the Streamlit server was restarted (imported CSS module was cached). Fixed by restarting.
4. Dashboard cards had uneven heights, which misaligned the Open buttons. Fixed with a minimum height.
5. Score ring showed "44%" while the formula showed 43.8%. Changed the ring to show 43.8%.

## 7. Results and observations *(write in your own words after you test)*
- What worked well:
- What the rule-based approach cannot do:
- What you would improve with a live AI model:

## 8. Your own challenges and solutions *(only real ones)*
| Challenge | What you did | Result |
|---|---|---|
| | | |
