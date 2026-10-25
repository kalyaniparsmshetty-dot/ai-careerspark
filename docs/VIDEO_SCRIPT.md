# Video Presentation Script (target 3 minutes, minimum 2)

Speak slowly and naturally. About 130 words per minute: this script is about 430 words, so it runs roughly 3 minutes with the demo pauses.
Text in **[brackets]** is for you to do or fill in. Only say a challenge story if it really happened to you.

## 1. Introduction (0:00 to 0:20) *screen: Welcome page*
"Hello, my name is **[your name]**. This is my project for the AI Growth and Automation Associate assessment. It is called AI CareerSpark, an AI-powered career assistant. The idea is simple: understand the role, improve your skills, and prepare with confidence."

## 2. The problem (0:20 to 0:40)
"When I look at job postings, it is hard to know what they really ask for, whether my resume matches, and what I should practise. Fresh graduates and people changing careers feel this the most. So I built one place that helps with all of that, for free."

## 3. AI tools and why (0:40 to 1:05)
"I used Claude as my AI development partner. I used it to plan the architecture, write the code, find bugs, and prepare the tests and documentation. **[Add ChatGPT here only if you really used it.]** To be clear and honest: AI helped me build the project, but the app itself uses rule-based Python. It does not call a live AI model, so it is free and needs no API key."

## 4. Prompt engineering (1:05 to 1:30) *screen: docs/PROMPT_LOG.md*
"I kept a prompt log. My first prompts were short, and I improved them by adding specific requirements: results must depend on the real input, the score must follow a documented formula, empty and invalid input must show clear messages, and the app must be honest about its limits. **[Describe one real revision you made, using your own words.]**"

## 5. Technical approach (1:30 to 1:50) *screen: VS Code folder tree*
"The app uses Python and Streamlit. The logic is in the careerspark folder: a skills list, and an analyzer module that finds skills with regular expressions, calculates the score, and generates interview questions from templates. The design uses custom CSS. I also wrote sixteen automated tests."

## 6. Challenges (1:50 to 2:05)
"**[Only if true for you:]** One challenge was **[real challenge]**. I solved it by **[what you really did]**."

## 7. Live demo (2:05 to 2:50) *screen: the running app*
"Let me show it working. I click Get Started. On the Job Description Analyzer I load the sample and click Analyze. Here are the skills, responsibilities and keywords found in this text.
Next, the Resume Matcher. I click Compare skills. The score is 43.8 percent. It is calculated as 7 matched skills divided by 16 job skills, and the page explains this is only an estimate, not a hiring prediction. Here are the missing skills and suggestions.
In Interview Preparation I generate questions. These are labelled as rule-based templates, with difficulty levels and sample answers.
In Resume Improvement, the wording is improved without adding any new facts, and I can copy it with this button. The About page explains how it works and its limits."

## 8. Outcome and limits (2:50 to 3:10)
"The final result is a working app with seven pages, tests, and documentation. Its limits are that it only recognises skills in its built-in list and can miss different wording. In the future, a live AI model could understand meaning better. Thank you for watching. The code is on GitHub: **[say your real link only after you checked it works]**."

## Demonstration checklist (what to show while recording)
- [ ] App already running (`streamlit run app.py`) and browser zoomed to about 110%
- [ ] Welcome page, then Get Started
- [ ] Dashboard and sidebar
- [ ] Analyzer: Load sample, Analyze job, scroll through results, click Download
- [ ] Analyzer: click Analyze with an empty box to show the validation message
- [ ] Matcher: Load sample, Compare skills, point to the formula and the disclaimer
- [ ] Interview: Load sample, Generate, open two questions
- [ ] Improve: Load sample, Improve wording, click the copy icon
- [ ] About and Help page
- [ ] `docs/PROMPT_LOG.md` showing your real prompts
- [ ] Terminal showing `python -m pytest -q` with passing tests (run it on your computer first)
- [ ] GitHub repository page

Recording tips: Windows Game Bar (Win + G) or OBS Studio, both free. Close other tabs, silence notifications, record once to test the sound, and check the final length is over 2 minutes.
