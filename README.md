# AI CareerSpark: AI-Powered Career Assistant

🚀 Live Demo: https://ai-careerspark-aubjueeu3dni9zhdj2g5rr.streamlit.app/

*Understand the role. Improve your skills. Prepare with confidence.*

A free, beginner-friendly web app (Python + Streamlit) that helps fresh graduates, entry-level applicants and career changers to:

1. **Analyze a job description** (skills, responsibilities, experience, keywords, preparation areas)
2. **Match a resume to a job** (explainable, formula-based score)
3. **Practise interviews** (technical, HR and scenario questions with sample answers)
4. **Improve resume wording** (clearer phrasing, no invented facts, copy button)

## Honest statement about AI

| Part | What it is |
|---|---|
| Developing this project | **AI-assisted.** Claude was used to plan, write, review and test the code (see `docs/PROMPT_LOG.md`). |
| Features inside the app | **Rule-based Python**: keyword lists, regular expressions and templates. |
| Live AI model inside the app | **None.** The app makes no calls to any AI service and needs no API key. |

Because it is rule-based, it is free, works offline after install, and gives repeatable results. The trade-off is that it only recognises skills in its built-in list (about 90) and can miss different wording.

## Folder structure

```
ai-careerspark/
├── app.py                    Streamlit interface: all 7 pages and buttons
├── careerspark/
│   ├── analyzer.py           Analysis logic: validation, skill finding, scoring, questions, rewriting
│   ├── skills_data.py        Skill list, role profiles, question and answer templates
│   ├── samples.py            Fictional sample inputs used by the "Load sample" buttons
│   └── styles.py             CSS for the visual design
├── .streamlit/config.toml    Theme colours and Streamlit settings
├── tests/                    16 automated tests (logic and app flow)
├── sample_inputs/            The same samples as plain .txt files
├── docs/
│   ├── WINDOWS_SETUP.md      Step-by-step setup, GitHub upload, free deployment
│   ├── PROMPT_LOG.md         Prompt documentation (templates + suggestions + your real prompts)
│   ├── TESTING.md            Test report: done by the developer vs. to be done by you
│   ├── VIDEO_SCRIPT.md       2+ minute presentation script and recording checklist
│   └── SUBMISSION_CHECKLIST.md
├── requirements.txt          streamlit
└── requirements-dev.txt      streamlit + pytest (only needed to run tests)
├── Screenshots/
    ├── dashboard.png        
    ├── job-description.png           
    ├── resume-and-skills matcher.png
    ├── interview-preparation.png
    ├── resume improvement.png
    ├── about-help.png 
 
## Quick start (Windows, PowerShell, inside the project folder)

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```
The app opens at http://localhost:8501. Full beginner steps: `docs/WINDOWS_SETUP.md`.

## How the match score works

`score = (skills in the job description that are also found in the resume) / (skills found in the job description) x 100`

Example: 7 matched / 16 job skills x 100 = 43.8%. All skills count equally. It is a text-based estimate, **not** a prediction of hiring success.

## Data handling
No login, database or file storage in this app's code. Text lives in the session while the page is open. There is no encryption or deletion feature, and a hosting provider may keep its own logs. Do not paste sensitive personal details.

## Run the tests
```powershell
pip install -r requirements-dev.txt
python -m pytest -q
```

## Limitations
Recognises only built-in skills; matches words, not meaning; sample answers are generic templates; title and responsibility detection depends on the text layout.
