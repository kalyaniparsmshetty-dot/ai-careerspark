# Windows Setup Guide (for beginners)

Type commands in **PowerShell** unless told otherwise. Press Enter after each command.

## 1. Download the project
Download `ai-careerspark.zip` from the chat and save it to your Downloads folder.

## 2. Extract the ZIP
Right-click the ZIP, choose **Extract All…**, then **Extract**. Move the extracted `ai-careerspark` folder to a simple place such as `C:\Projects\ai-careerspark`.

## 3. Open the folder in VS Code
1. Install VS Code from https://code.visualstudio.com if you do not have it (free).
2. Open VS Code, choose **File → Open Folder…**, select `ai-careerspark`, click **Select Folder**.
3. Choose **Terminal → New Terminal**. A PowerShell panel opens at the bottom, already inside the project folder.

## 4. Check that Python is installed
```powershell
py --version
```
Success looks like `Python 3.11.x` (3.10 or newer is fine). If you see "not recognized", install Python from https://www.python.org/downloads/ and **tick "Add python.exe to PATH"** on the first screen, then close and reopen VS Code.

## 5. Install the dependencies
```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```
After the second command you should see `(.venv)` at the start of the line. The install ends with `Successfully installed streamlit-…`.

*If activation says "running scripts is disabled":* run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`, answer `Y`, and repeat the activation command.

## 6. Run the app
```powershell
streamlit run app.py
```
Success: the terminal shows `Local URL: http://localhost:8501` and your browser opens. If Streamlit asks for an email, press Enter to skip. Stop the app with `Ctrl + C`.

## 7. Test each feature (about 10 minutes)
Follow `docs/TESTING.md`, section "Tests for you to perform". Quick version:
1. Click **Get Started**. The dashboard opens.
2. **Job Description Analyzer:** click **Load sample**, then **Analyze job**. Results appear. Click **Download results**.
3. **Matcher:** click **Load sample**, then **Compare skills**. You should see **43.8%** with the formula.
4. **Interview Preparation:** click **Load sample**, **Generate questions**, open a question.
5. **Resume Improvement:** click **Load sample**, **Improve wording**, use the copy icon on the "Improved wording" box and paste into Notepad.
6. **About and Help** opens. Try clicking **Analyze job** with an empty box to see the error message.

## 8. Fixing common errors
| Message | Fix |
|---|---|
| `'streamlit' is not recognized` | The virtual environment is not active. Run `.venv\Scripts\Activate.ps1`, or use `py -m streamlit run app.py`. |
| `No module named 'careerspark'` | You are not inside the project folder. Run `cd C:\Projects\ai-careerspark` (use your real path). |
| Port already in use | `streamlit run app.py --server.port 8502` |
| Browser does not open | Open http://localhost:8501 yourself. |
| `TypeError … unexpected keyword 'icon'` or `wrap_lines` | Old Streamlit. Run `pip install --upgrade streamlit`. |
| Fonts look different | The Google font needs internet. The app falls back to system fonts. This is normal offline. |

## 9. Upload to GitHub (free)
1. Create a free account at https://github.com.
2. Click **+ → New repository**. Name it `ai-careerspark`, choose **Public**, do **not** tick "Add a README" (the project already has one), click **Create repository**.
3. Install Git from https://git-scm.com/download/win if `git --version` fails.
4. In the VS Code terminal (project folder), run, replacing `YOUR-USERNAME`:
```powershell
git init
git add .
git commit -m "AI CareerSpark: initial version"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/ai-careerspark.git
git push -u origin main
```
5. GitHub may open a browser window to sign in. After success, refresh the repository page: you should see `app.py`, `README.md` and the other files.
6. **Verify access:** open the repository URL in a private/incognito window. If you can see the files without signing in, a reviewer can too.

*Easier alternative:* on the repository page choose **Add file → Upload files**, drag in the *contents* of the folder, and click **Commit changes**. (`.gitignore` and `.streamlit` are hidden folders/files; use the Git commands above if the browser upload skips them.)

## 10. Free deployment (attempt)
Streamlit Community Cloud has offered free hosting for public GitHub apps. **Check the current terms at https://streamlit.io/cloud before relying on it.** I could not test deployment for you.
1. Go to https://share.streamlit.io and sign in with GitHub.
2. Click **Create app**, choose your repository, branch `main`, main file `app.py`.
3. Click **Deploy**. The first build takes a few minutes.
4. When it finishes, copy the `https://….streamlit.app` address and open it in an incognito window to check it works.
5. Free apps may "go to sleep" after inactivity and show a "wake up" button. Open the link yourself shortly before the review.

**If deployment is unavailable or fails:** submit the public GitHub link (it has the code, README and docs), and say in your submission that the app runs locally with the three commands in the README. Also show it running in your video. Check the assessment instructions to confirm that is accepted.

Only put a live URL in your submission after you have opened it and confirmed it works.
