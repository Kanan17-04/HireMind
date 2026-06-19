# backend/app/ml/skills_db.py
#
# Single source of truth for the skills vocabulary.
# Imported by JDExtractor, ResumeExtractor, and any future matching agents
# so that additions here are automatically picked up everywhere.

SKILLS_DB: list[str] = [
    # --- Languages ---
    "python", "java", "scala", "go", "rust", "c++", "c#", "ruby",
    "typescript", "javascript", "kotlin", "swift", "r",

    # --- Query / Data ---
    "sql", "nosql", "graphql",

    # --- Cloud ---
    "aws", "gcp", "azure",

    # --- DevOps / Infra ---
    "docker", "kubernetes", "terraform", "ansible", "jenkins",
    "ci/cd", "linux", "bash", "powershell",

    # --- Frontend ---
    "react", "angular", "vue", "next.js", "node.js",

    # --- Backend Frameworks ---
    "fastapi", "django", "flask", "spring", "express",

    # --- Databases ---
    "mongodb", "postgresql", "mysql", "redis", "elasticsearch",

    # --- Messaging ---
    "kafka", "rabbitmq", "celery",

    # --- Version Control ---
    "git", "github", "gitlab", "bitbucket",

    # --- ML / Data Science ---
    "machine learning", "deep learning", "nlp", "computer vision",
    "pandas", "numpy", "scikit-learn", "tensorflow", "pytorch",

    # --- Architecture / Process ---
    "rest", "microservices", "agile", "scrum",

    # Product
    "product management","product strategy","roadmap","jira","confluence",

    # Cloud
    "google cloud","cloud computing","gcp","sre",
    # Data
    "power bi","tableau","excel","statistics",
    # AI
    "llm","rag","langgraph","crewai","prompt engineering","generative ai",
    # Business
    "stakeholder management","business analysis","kpi","market research",
    # Security
    "cybersecurity","security","identity management",
]