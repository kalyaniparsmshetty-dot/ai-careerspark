# Testing Report

## A. Tests actually performed during development (sandbox: Linux, Python 3.12.3, Streamlit 1.66.1)

| # | Test | Method | Result |
|---|---|---|---|
| 1 | 10 logic tests: empty, short and symbols-only rejected; long text trimmed with notice; skill-detection edge cases (Java vs JavaScript, SQL vs MySQL, C++/C#, "excellent" is not Excel); different job descriptions give different skills; score equals matched/job skills x 100; different resumes give different scores; no skills found gives 0 and empty lists; questions differ by title and by job description; rewriter adds no digits or skills | `python -m pytest` (tests/test_analyzer.py) | **10 passed** |
| 2 | 6 app-flow tests: welcome opens; Get Started works; all 7 pages render without exceptions; empty-input errors show; sample then analyse works; matcher gives 43.8% for the sample and Clear resets; interview and improve flows; job description kept when moving between pages | Streamlit AppTest (tests/test_app.py) | **6 passed** |
| 3 | Server starts and health check returns HTTP 200 | `streamlit run app.py` + curl | Pass |
| 4 | In a real headless Chromium: all pages opened via the sidebar with no error panels and no JavaScript errors; analyzer, interview downloads produced `job_analysis.txt` and `interview_practice.txt`; empty matcher shows 2 error messages; interview sample shows sample answers | Playwright script | Pass |
| 5 | Copy icon on the "Improved wording" box copied the improved text to the clipboard | Playwright (clipboard read) | Pass |
| 6 | Mobile width 390 px: no horizontal scrolling; columns stack; sidebar collapses behind the » control | Playwright screenshots + scroll-width check | Pass |
| 7 | Desktop 1280 px layout reviewed visually for welcome, dashboard, analyzer, matcher | Screenshots | Looked correct |

## B. NOT verified: you must check these on your computer
- [ ] Install and run on **Windows** with the steps in `docs/WINDOWS_SETUP.md` (tested on Linux only).
- [ ] Visual check in your own browser (Chrome or Edge). Google Fonts could not load in the sandbox; the app uses a fallback font there. Confirm "Plus Jakarta Sans" appears on your computer with internet.
- [ ] Download buttons for matcher and resume-wording results (analyzer and interview downloads were tested; the others use the same mechanism but were not clicked).
- [ ] Test on a real phone or browser dev-tools mobile view (F12, device toolbar).
- [ ] GitHub upload and public access in an incognito window.
- [ ] Streamlit Community Cloud deployment (not attempted).
- [ ] Your own inputs: paste a real job description and resume and read the results for sense.

## C. Manual test checklist (tick as you go)
| Page | Action | Expected |
|---|---|---|
| Welcome | Click Get Started | Dashboard opens with sidebar |
| Dashboard | Click each Open button and each quick action | Correct page opens; sample actions fill the text boxes |
| Analyzer | Click Analyze with empty box | Red message: paste the job description |
| Analyzer | Type "hello world", Analyze | Message: too short (2 words) |
| Analyzer | Load sample, Analyze | Role "Junior Data Analyst", 16 skills, responsibilities, keywords |
| Analyzer | Replace with Medical Records sample (from `sample_inputs`) | Different skills (HIPAA, EHR) and no SQL |
| Matcher | Load sample, Compare | 43.8% (7 / 16 skills) |
| Matcher | Delete "Python, Pandas, Excel" from the resume and compare | Score goes down |
| Matcher | Clear | Both boxes and results empty |
| Interview | Enter only "Nurse", Generate | Questions about patient care and records; source says job title |
| Interview | Enter only "zzz", Generate | Warning about no known skills, with HR questions |
| Improve | Load sample, Improve | Bullets starting with Managed / Contributed to; no invented numbers |
| Improve | Click copy icon, paste in Notepad | Improved text appears |
| About | Read the page | Says the app is rule-based, explains the formula and data handling |
| Mobile view | Resize the browser narrow | No sideways scrolling; sidebar opens with the » button |

## D. Known limitations found while testing
- Skills outside the built-in list (about 90) are ignored.
- A broad term can count twice (for example "clinical documentation" counts as both Clinical Documentation and Documentation).
- Title and responsibility detection depend on layout; unusual formats may show "Not clearly stated".
- Rewriting uses simple rules and may need manual correction; always review it.
