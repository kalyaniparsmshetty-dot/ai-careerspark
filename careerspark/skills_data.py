"""Skill taxonomy and question templates used by the rule-based analyzer.

Everything in this file is plain Python data. No AI model is involved.
Each skill has a canonical name and a list of aliases that count as the same skill.
"""

# category -> {canonical skill name: [aliases]}
SKILLS = {
    "Programming": {
        "Python": ["python", "python3"],
        "Java": ["java", "core java"],
        "JavaScript": ["javascript", "js", "ecmascript"],
        "TypeScript": ["typescript"],
        "C++": ["c++"],
        "C#": ["c#"],
        "R": ["r programming", "r language", "rstudio"],
        "PHP": ["php"],
        "Go": ["golang"],
        "Kotlin": ["kotlin"],
        "Bash": ["bash", "shell scripting", "shell script"],
    },
    "Web Development": {
        "HTML": ["html", "html5"],
        "CSS": ["css", "css3"],
        "React": ["react", "react.js", "reactjs"],
        "Angular": ["angular", "angularjs"],
        "Vue": ["vue", "vue.js", "vuejs"],
        "Node.js": ["node.js", "nodejs"],
        "Django": ["django"],
        "Flask": ["flask"],
        "REST APIs": ["rest api", "restful", "api", "web services"],
        "Responsive Design": ["responsive design", "responsive web"],
    },
    "Data and Analytics": {
        "SQL": ["sql", "t-sql", "pl/sql"],
        "MySQL": ["mysql"],
        "PostgreSQL": ["postgresql", "postgres"],
        "MongoDB": ["mongodb"],
        "Excel": ["excel", "ms excel", "microsoft excel", "spreadsheet", "google sheets"],
        "Power BI": ["power bi", "powerbi"],
        "Tableau": ["tableau"],
        "Data Analysis": ["data analysis", "data analytics", "analyze data", "analyse data", "analysing data", "analyzing data", "data analyst"],
        "Data Visualization": ["data visualization", "data visualisation", "dashboard", "data viz"],
        "Statistics": ["statistics", "statistical", "hypothesis testing"],
        "Pandas": ["pandas"],
        "NumPy": ["numpy"],
        "Data Cleaning": ["data cleaning", "data cleansing", "data wrangling", "data preparation"],
        "ETL": ["etl", "data pipeline"],
        "Reporting": ["reporting", "report"],
    },
    "AI and Machine Learning": {
        "Machine Learning": ["machine learning", "ml"],
        "Deep Learning": ["deep learning", "neural network"],
        "Artificial Intelligence": ["artificial intelligence"],
        "NLP": ["nlp", "natural language processing"],
        "TensorFlow": ["tensorflow"],
        "PyTorch": ["pytorch"],
        "Scikit-learn": ["scikit-learn", "sklearn", "scikit learn"],
        "Prompt Engineering": ["prompt engineering", "prompt design", "prompting"],
        "Automation": ["automation", "automate", "automating", "workflow automation"],
    },
    "Cloud and DevOps": {
        "Git": ["git", "version control"],
        "GitHub": ["github"],
        "Docker": ["docker", "containerization", "container"],
        "Kubernetes": ["kubernetes", "k8s"],
        "AWS": ["aws", "amazon web services"],
        "Azure": ["azure"],
        "Google Cloud": ["google cloud", "gcp"],
        "Linux": ["linux", "unix"],
        "CI/CD": ["ci/cd", "continuous integration", "continuous delivery", "jenkins"],
    },
    "Software Practice": {
        "Software Testing": ["software testing", "unit test", "test case", "qa testing", "manual testing", "test automation", "quality assurance", "testing"],
        "Debugging": ["debugging", "troubleshooting", "bug fixing"],
        "Agile": ["agile", "scrum", "kanban", "sprint"],
        "Data Structures": ["data structures", "algorithms"],
        "Object-Oriented Programming": ["object-oriented", "object oriented", "oop"],
        "Documentation": ["documentation", "technical writing", "documenting"],
    },
    "Networking and Security": {
        "Networking": ["networking", "tcp/ip", "network administration"],
        "Cybersecurity": ["cybersecurity", "cyber security", "information security", "infosec"],
        "Technical Support": ["technical support", "help desk", "helpdesk", "it support", "service desk"],
    },
    "Healthcare": {
        "Patient Care": ["patient care", "patient support", "bedside manner"],
        "Electronic Health Records": ["electronic health records", "electronic medical records", "ehr", "emr"],
        "HIPAA": ["hipaa", "patient privacy", "patient confidentiality"],
        "Medical Terminology": ["medical terminology", "clinical terminology"],
        "Medical Coding": ["medical coding", "icd-10", "icd 10", "cpt coding", "medical billing"],
        "Clinical Documentation": ["clinical documentation", "medical record", "charting"],
        "Healthcare Data": ["healthcare data", "health data", "health informatics", "clinical data"],
        "Infection Control": ["infection control", "sterile technique", "hygiene protocol"],
        "Scheduling": ["appointment scheduling", "scheduling appointment", "scheduling"],
        "Basic Life Support": ["bls", "basic life support", "cpr", "first aid"],
    },
    "Business and Tools": {
        "Project Management": ["project management", "project coordination", "managing projects"],
        "Stakeholder Management": ["stakeholder management", "stakeholder"],
        "Microsoft Office": ["microsoft office", "ms office", "office suite", "powerpoint"],
        "CRM": ["crm", "salesforce", "hubspot"],
        "Research": ["research", "market research"],
        "Content Writing": ["content writing", "copywriting", "content creation"],
        "Social Media": ["social media", "social media marketing"],
        "SEO": ["seo", "search engine optimization"],
    },
    "Soft Skills": {
        "Communication": ["communication", "communicate", "communicating"],
        "Teamwork": ["teamwork", "team player", "collaboration", "collaborate", "collaborative", "work in a team", "cross-functional"],
        "Problem Solving": ["problem solving", "problem-solving", "solve problems", "analytical thinking", "analytical skill"],
        "Leadership": ["leadership", "lead a team", "team lead", "mentoring"],
        "Time Management": ["time management", "meet deadlines", "prioritization", "prioritisation", "deadline"],
        "Critical Thinking": ["critical thinking"],
        "Adaptability": ["adaptability", "adaptable", "fast learner", "quick learner", "willingness to learn", "eager to learn"],
        "Attention to Detail": ["attention to detail", "detail-oriented", "detail oriented"],
        "Customer Service": ["customer service", "customer support", "customer-facing", "client service"],
        "Presentation": ["presentation skill", "presenting", "public speaking"],
    },
}

SKILL_CATEGORY = {skill: cat for cat, group in SKILLS.items() for skill in group}

# Words that look important but carry no meaning for keyword lists.
STOPWORDS = set("""
a about above after again all also am an and any are as at be because been before being below between both but by can could
did do does doing down during each few for from further had has have having he her here hers him his how i if in into is it its
just me more most my no nor not now of off on once only or other our out over own same she should so some such than that the
their them then there these they this those through to too under until up very was we were what when where which while who whom
why will with would you your yours etc per via within across including include includes
""".split())

GENERIC_JOB_WORDS = set("""
job role position candidate candidates company team work working experience ability skills skill strong good great excellent
required requirements preferred responsibilities responsible duties looking join opportunity must should will years year plus
knowledge understanding application applications related relevant well new like help support using use used make able best
need needs apply employer employees employee business client clients day days time part full
""".split())

ACTION_VERBS = set("""
analyze analyse build create design develop implement maintain manage monitor prepare perform support assist coordinate
collaborate review test write document deliver lead plan organize organise identify ensure conduct improve troubleshoot
respond provide update track report research communicate present train schedule assess resolve optimize optimise
automate integrate deploy configure
""".split())

# Preparation advice by skill category.
PREP_BY_CATEGORY = {
    "Programming": "Practise small coding exercises in the languages listed and be ready to explain your code step by step.",
    "Web Development": "Build or review a small web page or app and be ready to explain how the pieces fit together.",
    "Data and Analytics": "Practise cleaning and summarising a small public dataset, and be ready to explain what the numbers mean.",
    "AI and Machine Learning": "Review core ideas (training vs testing data, overfitting, evaluation) and be ready to discuss one small project.",
    "Cloud and DevOps": "Revise basic Git commands and how code moves from a laptop to a running service.",
    "Software Practice": "Revise how you test and debug your work, and how teams plan work in sprints.",
    "Networking and Security": "Revise the basics of how networks work and common security habits.",
    "Healthcare": "Revise patient privacy rules, accurate record keeping and the basic terminology used in the role.",
    "Business and Tools": "Prepare examples of using these tools or processes to get a task done.",
    "Soft Skills": "Prepare two or three short stories (situation, action, result) from study, projects or part-time work.",
}

# Rough role profiles used when only a job title is supplied (matched by keyword in the title).
ROLE_PROFILES = {
    "data analyst": ["SQL", "Excel", "Data Analysis", "Data Visualization", "Python", "Statistics", "Communication"],
    "data scientist": ["Python", "Machine Learning", "Statistics", "SQL", "Data Visualization", "Pandas"],
    "machine learning": ["Python", "Machine Learning", "Statistics", "Deep Learning", "Pandas", "Scikit-learn"],
    "frontend": ["HTML", "CSS", "JavaScript", "React", "Responsive Design", "Git"],
    "front end": ["HTML", "CSS", "JavaScript", "React", "Responsive Design", "Git"],
    "backend": ["Python", "SQL", "REST APIs", "Git", "Software Testing", "Docker"],
    "web": ["HTML", "CSS", "JavaScript", "Responsive Design", "Git", "REST APIs"],
    "software": ["Data Structures", "Git", "Debugging", "Software Testing", "Object-Oriented Programming", "Teamwork"],
    "developer": ["Git", "Debugging", "Software Testing", "REST APIs", "Teamwork", "Problem Solving"],
    "automation": ["Automation", "Python", "Prompt Engineering", "Problem Solving", "Documentation", "Communication"],
    "ai": ["Python", "Machine Learning", "Prompt Engineering", "Automation", "Problem Solving", "Communication"],
    "tester": ["Software Testing", "Debugging", "Documentation", "Agile", "Attention to Detail", "Communication"],
    "qa": ["Software Testing", "Debugging", "Documentation", "Agile", "Attention to Detail", "Communication"],
    "support": ["Technical Support", "Debugging", "Customer Service", "Communication", "Documentation", "Problem Solving"],
    "network": ["Networking", "Linux", "Cybersecurity", "Technical Support", "Documentation", "Problem Solving"],
    "security": ["Cybersecurity", "Networking", "Linux", "Problem Solving", "Documentation", "Attention to Detail"],
    "cloud": ["AWS", "Linux", "Docker", "Git", "Networking", "CI/CD"],
    "devops": ["Linux", "Docker", "Git", "CI/CD", "Automation", "AWS"],
    "nurse": ["Patient Care", "Clinical Documentation", "Infection Control", "Basic Life Support", "Communication", "Teamwork"],
    "medical": ["Medical Terminology", "Clinical Documentation", "HIPAA", "Electronic Health Records", "Attention to Detail", "Communication"],
    "clinical": ["Clinical Documentation", "Patient Care", "HIPAA", "Electronic Health Records", "Attention to Detail", "Teamwork"],
    "healthcare": ["Patient Care", "HIPAA", "Electronic Health Records", "Healthcare Data", "Communication", "Teamwork"],
    "health": ["Healthcare Data", "HIPAA", "Electronic Health Records", "Data Analysis", "Communication", "Attention to Detail"],
    "project": ["Project Management", "Stakeholder Management", "Agile", "Communication", "Time Management", "Documentation"],
    "marketing": ["Social Media", "SEO", "Content Writing", "Data Analysis", "Communication", "Research"],
}

# Handwritten technical question templates: skill -> (question, sample answer, difficulty)
SKILL_QUESTIONS = {
    "Python": ("What is the difference between a list and a tuple in Python?",
               "A list can be changed after it is created, while a tuple cannot. I use a list when the items will change, such as a growing set of results, and a tuple for fixed values such as coordinates.", "Beginner"),
    "SQL": ("What is the difference between INNER JOIN and LEFT JOIN in SQL?",
            "INNER JOIN returns only rows that have a match in both tables. LEFT JOIN returns every row from the left table and fills in NULL where the right table has no match. I would use LEFT JOIN to find customers with no orders.", "Beginner"),
    "Excel": ("How would you use VLOOKUP or XLOOKUP, and what are common mistakes?",
              "They search for a value in one column and return a related value from another column. Common mistakes are using an approximate match by accident, a lookup value that has extra spaces, or a changed column range. I check the match type and clean the data first.", "Beginner"),
    "Java": ("What are the four main principles of object-oriented programming?",
             "Encapsulation (hiding data behind methods), inheritance (reusing behaviour from a parent class), polymorphism (one interface, many forms) and abstraction (showing only what is necessary).", "Beginner"),
    "JavaScript": ("What is the difference between var, let and const?",
                   "var is function-scoped and can be redeclared. let and const are block-scoped. const cannot be reassigned. In modern code I use const by default and let when the value must change.", "Beginner"),
    "HTML": ("Why is semantic HTML important?",
             "Tags such as header, nav, main and article describe the meaning of content. This helps screen readers, search engines and other developers understand the page.", "Beginner"),
    "CSS": ("How do Flexbox and CSS Grid differ?",
            "Flexbox arranges items in one direction (a row or a column) and is good for components. Grid controls rows and columns together and is good for page layouts.", "Intermediate"),
    "React": ("What is the difference between props and state in React?",
              "Props are inputs passed from a parent component and should not be changed by the child. State is data owned by a component that can change and cause the component to re-render.", "Intermediate"),
    "Git": ("What is the difference between git commit, git push and git pull?",
            "commit saves a snapshot of changes to my local repository, push uploads my commits to a remote repository such as GitHub, and pull downloads and merges new commits from the remote.", "Beginner"),
    "Machine Learning": ("What is overfitting and how can you reduce it?",
                         "Overfitting happens when a model learns the training data too closely, including noise, and performs poorly on new data. It can be reduced with more data, simpler models, regularisation and checking performance on a separate test set.", "Intermediate"),
    "Power BI": ("How would you design a dashboard for a non-technical audience?",
                 "I would start with the questions the audience needs answered, show a few key measures at the top, use simple charts with clear titles, add filters only where useful, and avoid clutter.", "Intermediate"),
    "Tableau": ("When would you use a bar chart instead of a line chart?",
                "A bar chart compares categories, such as sales by region. A line chart shows change over time, such as sales by month.", "Beginner"),
    "Statistics": ("What is the difference between mean and median, and when is median better?",
                   "The mean is the average and the median is the middle value. The median is better when the data has extreme values, such as salaries, because outliers pull the mean up or down.", "Beginner"),
    "Data Analysis": ("Walk me through the steps you would take to analyse a new dataset.",
                      "I would first understand the question, then check the data for missing values and errors, clean it, explore it with summaries and charts, answer the question, and finally explain the findings and any limits in simple language.", "Intermediate"),
    "Data Cleaning": ("How would you handle missing values in a dataset?",
                      "First I would find out why values are missing. Depending on the situation I might remove the rows, fill them with a sensible value such as the median, or flag them. I would document the choice because it can affect results.", "Intermediate"),
    "REST APIs": ("What is a REST API and what do the GET and POST methods do?",
                  "A REST API lets programs communicate over HTTP. GET requests data without changing it, and POST sends data to create something new on the server.", "Beginner"),
    "Software Testing": ("What is the difference between unit testing and integration testing?",
                         "Unit tests check one small piece of code in isolation. Integration tests check that several parts work correctly together, such as code and a database.", "Beginner"),
    "Debugging": ("Describe your process for finding the cause of a bug.",
                  "I try to reproduce it reliably, read the error message, narrow down where it happens using prints or a debugger, form a theory, test one change at a time, and then add a test so it does not return.", "Beginner"),
    "Docker": ("What problem does Docker solve?",
               "It packages an application with its dependencies in a container so it runs the same way on any machine, which avoids the 'it works on my computer' problem.", "Beginner"),
    "Linux": ("Which basic Linux commands do you use most and what do they do?",
              "ls lists files, cd changes directory, cat shows file content, grep searches text, and chmod changes permissions. If unsure, I check the manual with man.", "Beginner"),
    "AWS": ("What is the difference between object storage and a virtual server in the cloud?",
            "Object storage (such as S3) stores files and is accessed over the network. A virtual server (such as EC2) is a computer you can run programs on.", "Intermediate"),
    "Networking": ("What happens when you type a website address into a browser?",
                   "The browser asks DNS for the IP address, opens a connection to that server, sends an HTTP request, receives the response and renders the page.", "Intermediate"),
    "Cybersecurity": ("What is phishing and how can people protect themselves?",
                      "Phishing is a message that tricks someone into sharing sensitive information or clicking a harmful link. Protection includes checking the sender, not clicking unexpected links, and using multi-factor authentication.", "Beginner"),
    "Agile": ("What is a sprint in Scrum?",
              "A sprint is a short, fixed period, usually one to four weeks, in which a team completes a planned set of work and then reviews the result.", "Beginner"),
    "Prompt Engineering": ("What makes a prompt to an AI assistant effective?",
                           "A clear goal, relevant context, the format wanted, constraints, and examples. I then check the answer and refine the prompt based on what was missing or wrong.", "Beginner"),
    "Automation": ("How would you decide whether a task is worth automating?",
                   "I would look at how often it is repeated, how long it takes, how error-prone it is, and how stable the steps are. Frequent, rule-based tasks are good candidates.", "Intermediate"),
    "HIPAA": ("Why is patient privacy important and how would you protect it at work?",
              "Patients share sensitive information on the basis of trust, and privacy laws require it to be protected. I would access only the information I need, avoid discussing patients in public areas, and follow the organisation's procedures.", "Beginner"),
    "Electronic Health Records": ("Why is accurate record keeping important in an electronic health record system?",
                                  "Clinicians rely on records to make safe decisions, so errors can affect care. I would double-check entries, use approved terms and follow the organisation's documentation process.", "Beginner"),
    "Patient Care": ("How would you support a patient who is anxious or upset?",
                     "I would listen without interrupting, speak calmly and clearly, explain what will happen next, and involve a senior colleague if the situation is beyond my role.", "Beginner"),
    "Medical Terminology": ("How do you learn and remember unfamiliar medical terms?",
                            "I break terms into prefix, root and suffix, keep a glossary, and check unclear terms with a reliable reference or a colleague rather than guessing.", "Beginner"),
    "Project Management": ("How do you keep a project on track?",
                           "I break work into tasks, set owners and deadlines, review progress regularly, raise risks early and communicate changes to stakeholders.", "Intermediate"),
    "Customer Service": ("How would you handle a customer who is unhappy with a service?",
                         "I would listen, acknowledge the problem, apologise where appropriate, find a solution within my authority, and escalate if needed. I would follow up to make sure it was resolved.", "Beginner"),
    "Technical Support": ("How would you explain a technical problem to a non-technical user?",
                          "I would use plain words, avoid jargon, give one step at a time and confirm they understand before moving on.", "Beginner"),
    "Data Visualization": ("How do you choose the right chart for your data?",
                           "I start with the message: comparisons suit bar charts, trends over time suit line charts, and parts of a whole suit a simple pie or stacked bar. I keep charts uncluttered and clearly labelled.", "Beginner"),
}

HR_QUESTIONS = [
    ("Tell me about yourself.", "Beginner",
     "Start with who you are now (course, role or current focus), mention one or two relevant strengths or projects, and finish with why this role interests you. Keep it to about a minute.",
     "Use a present, past, future structure. Do not recite your whole resume."),
    ("Why do you want to work in this role and for this company?", "Beginner",
     "Say what you understand about the role, connect it to skills you have really built, and explain what you hope to learn.",
     "Read the job description and the company's website first so your answer is specific."),
    ("What are your strengths and weaknesses?", "Beginner",
     "Give one real strength with a short example. For a weakness, name a genuine one that you are actively improving and explain the steps you are taking.",
     "Avoid fake weaknesses such as 'I work too hard'."),
    ("Describe a time you worked in a team.", "Intermediate",
     "Use the STAR method: describe the Situation and Task, your Action, and the Result. Use a real example from study, a project or work.",
     "Say 'I' when describing your part and 'we' for team results."),
    ("Tell me about a time you made a mistake and what you learned.", "Intermediate",
     "Choose a real, small-to-moderate mistake, explain how you fixed it and what you now do differently.",
     "Focus on learning and action, not blame."),
    ("How do you handle tight deadlines or pressure?", "Intermediate",
     "Explain how you prioritise, break work into steps, communicate early if there is a risk, and ask for help when needed. Add a real example if you have one.",
     "Show calm, practical habits."),
    ("Where do you see yourself in a few years?", "Beginner",
     "Describe the skills you want to build and the kind of responsibility you hope to grow into, linked to this field.",
     "Be honest and show a wish to grow."),
    ("Do you have any questions for us?", "Beginner",
     "Ask about the team, how success is measured in the first months, and learning opportunities.",
     "Prepare at least two questions beforehand."),
]

SCENARIO_TEMPLATES = {
    "Data and Analytics": ("Your manager asks for a report by tomorrow, but you notice some numbers in the data look wrong. What do you do?",
                           "I would check the data source and look for the cause of the odd values. I would tell my manager early about the issue, explain what I found, and share what can be reported reliably now and what needs more time.", "Intermediate"),
    "Programming": ("You are given a task using a tool you have never used. How do you start?",
                    "I would read the official documentation, try a small example, break the task into steps, and ask a teammate if I get stuck after trying for a reasonable time.", "Beginner"),
    "Web Development": ("A user reports that a page looks broken on their phone. How would you investigate?",
                        "I would ask for the device and browser, reproduce it using browser developer tools in mobile view, find the CSS that causes it, fix it and test again on different screen sizes.", "Intermediate"),
    "AI and Machine Learning": ("A model you built gives good results in testing but poor results with real users. What might be wrong?",
                                "The training data may not match real-world data, the model may have overfitted, or the inputs may differ. I would compare the datasets, check for errors and collect more representative data.", "Advanced"),
    "Cloud and DevOps": ("A deployment fails right before a release. What steps would you take?",
                         "I would read the error logs, find what changed, roll back to the last working version if needed, inform the team, then fix and re-test the issue.", "Intermediate"),
    "Software Practice": ("You find a bug just before a release deadline. What do you do?",
                          "I would assess how serious it is, tell the team lead straight away, and agree whether to fix it, delay or release with a known limitation.", "Intermediate"),
    "Networking and Security": ("You suspect a colleague has opened a suspicious email. What do you do?",
                                "I would ask them to stop interacting with it, report it using the organisation's security process, and avoid deleting evidence until security staff advise.", "Intermediate"),
    "Healthcare": ("You notice a colleague has left a patient record open on a shared screen. What do you do?",
                   "I would lock the screen if appropriate, remind the colleague politely about privacy rules, and report it following the organisation's procedure if needed.", "Intermediate"),
    "Business and Tools": ("Two stakeholders give you conflicting priorities. How do you decide what to do first?",
                           "I would clarify the goals and deadlines, share the conflict openly with both, and ask my manager to help agree the priority.", "Intermediate"),
    "Soft Skills": ("A teammate is not completing their part of a shared task. What would you do?",
                    "I would speak to them privately to understand any problems, offer help, and agree a plan. If it continues, I would raise it with the team lead.", "Intermediate"),
}
