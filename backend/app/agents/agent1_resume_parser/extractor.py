import re


class ResumeExtractor:

    @staticmethod
    def extract_email(text: str):
        match = re.search(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            text,
        )
        return match.group(0) if match else ""

    @staticmethod
    def extract_phone(text: str):
        match = re.search(
            r"(?:\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}",
            text,
        )
        return match.group(0) if match else ""

    @staticmethod
    def extract_name(text: str):
        match = re.search(
            r"Full\s+Name\s*\|?\s*(.+)",
            text,
            re.IGNORECASE,
        )

        if match:
            return match.group(1).strip()

        lines = [
            line.strip()
            for line in text.split("\n")
            if line.strip()
        ]

        return lines[0] if lines else ""

    @staticmethod
    def get_section(
        text: str,
        start_pattern: str,
        end_patterns: list[str],
    ):
        start_match = re.search(
            start_pattern,
            text,
            re.IGNORECASE,
        )

        if not start_match:
            return ""

        start_idx = start_match.end()
        end_idx = len(text)

        for pattern in end_patterns:
            match = re.search(
                pattern,
                text[start_idx:],
                re.IGNORECASE,
            )

            if match:
                candidate_end = start_idx + match.start()

                if candidate_end < end_idx:
                    end_idx = candidate_end

        return text[start_idx:end_idx]

    @classmethod
    def extract_skills(cls, text: str):
        skills = set()

        # ---------- Method 1 ----------
        # Try Technical Skills section
        skills_section = cls.get_section(
            text,
            r"TECHNICAL\s+SKILLS\s*:?",
            [
                r"EDUCATION\s*:?",
                r"PROFESSIONAL\s+EXPERIENCE\s*:?",
            ],
        )

        if skills_section:
            for line in skills_section.split("\n"):
                parts = re.split(
                    r"[,|]",
                    line,
                )

                for part in parts:
                    part = part.strip()

                    if len(part) > 2 and len(part) < 60:
                        skills.add(part)

        # ---------- Method 2 ----------
        # Fallback for table-style resumes
        table_patterns = [
            r"Programming Language\s*\|(.+)",
            r"Java/J2EE Technologies\s*\|(.+)",
            r"Java Frameworks\s*\|(.+)",
            r"Application/Web Servers\s*\|(.+)",
            r"ORM Frameworks\s*\|(.+)",
            r"Web Technologies\s*\|(.+)",
            r"Spring Framework\s*\|(.+)",
            r"Database Server\s*\|(.+)",
            r"Web Services\s*\|(.+)",
            r"Version Control\s*\|(.+)",
            r"Build Tools\s*\|(.+)",
            r"Testing\s*\|(.+)",
            r"Languages?\s*:\s*(.+)",
            r"Databases?\s*:\s*(.+)",
            r"Operating Systems?\s*:\s*(.+)",  # FIX 3: also matches "Operating Systems"
            r"Other Software/Tools\s*:\s*(.+)",
            r"Technology\s*-\s*(.+)",
            r"Environment\s*:\s*(.+)",
        ]

        for pattern in table_patterns:
            matches = re.findall(
                pattern,
                text,
                re.IGNORECASE,
            )

            for match in matches:
                for skill in match.split(","):
                    skill = skill.strip()

                    if len(skill) > 1 and len(skill) < 60:
                        skills.add(skill)

        return sorted(list(skills))
    @staticmethod
    def extract_education_required(text: str):
        education_patterns = [
            r".*bachelor.*degree.*",
            r".*master.*degree.*",
            r".*phd.*",
            r".*doctorate.*",
            r".*b\.tech.*",
            r".*m\.tech.*",
            r".*b\.e.*",
            r".*m\.e.*",
            r".*b\.sc.*",
            r".*m\.sc.*",
        ]
        results = []
        for line in text.split("\n"):
            cleaned = line.strip()
            if not cleaned:
                continue
            for pattern in education_patterns:
                if re.search(pattern, cleaned, re.IGNORECASE):
                    if cleaned not in results:
                        results.append(cleaned)
                    break
        return results
    
    @staticmethod
    def extract_experience(text: str):
        summary_text = text[:3000]
        # FIX 2: single capture group so findall() returns strings, not tuples
        matches = re.findall(
            r"(?:\d+\+?\s*years?(?:\s+of\s+experience)?|(?:one|two|three|four|five|six|seven|eight|nine|ten)\s+years)",
            summary_text,
            re.IGNORECASE,
        )
        return list(set(matches))
    @classmethod
    def extract_projects(cls, text: str):
        # Match ONLY a PROJECTS heading
        header = re.search(
            r"^\s*PROJECTS?\s*:?\s*$",
            text,
            re.IGNORECASE | re.MULTILINE,
        )

        if not header:
            return []

        # FIX 1: added missing comma after the regex string
        project_section = cls.get_section(
            text,
            r"^\s*PROJECTS?\s*:?\s*$",
            [
                r"CERTIFICATIONS\s*:?",
                r"EDUCATION\s*:?",
                r"EXPERIENCE\s*:?",
            ],
        )

        if not project_section:
            return []

        projects = []

        for line in project_section.split("\n"):
            line = line.strip()

            if len(line) > 15:
                projects.append(line)

        return projects[:10]

    @staticmethod
    def extract_certifications(text: str):
        cert_section = re.search(
            r"CERTIFICATIONS?(.*?)(EDUCATION|EXPERIENCE|$)",
            text,
            re.IGNORECASE | re.DOTALL,
        )

        if not cert_section:
            return []

        certifications = []

        for line in cert_section.group(1).split("\n"):
            line = line.strip()

            if len(line) > 3:
                certifications.append(line)

        return certifications

    @classmethod
    def extract(
        cls,
        resume_text: str,
    ) -> dict:
        return {
            "name": cls.extract_name(resume_text),
            "email": cls.extract_email(resume_text),
            "phone": cls.extract_phone(resume_text),
            "skills": cls.extract_skills(resume_text),
            "projects": cls.extract_projects(resume_text),
            "experience": cls.extract_experience(resume_text),
            "education": cls.extract_education_required(resume_text),
            "certifications": cls.extract_certifications(resume_text),
        }