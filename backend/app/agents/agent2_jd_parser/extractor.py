# backend/app/agents/agent2_jd_parser/extractor.py

import re
from app.ml.skills_db import SKILLS_DB


class JDExtractor:

    @staticmethod
    def extract_job_title(text: str):
        skip_patterns = re.compile(
            r"^(job\s+description|position|role|title|about\s+the\s+(role|job|position))\s*:?$",
            re.IGNORECASE,
        )

        lines = [x.strip() for x in text.split("\n") if x.strip()]

        for line in lines:
            if not skip_patterns.match(line):
                return line

        return ""

    @staticmethod
    def extract_experience_required(text: str):
        matches = re.findall(
            r"(?:\d+\+?\s*(?:to|-)\s*\d+\+?\s*years?(?:\s+of\s+experience)?)"
            r"|(?:\d+\+?\s*years?(?:\s+of\s+experience)?)"
            r"|(?:(?:one|two|three|four|five|six|seven|eight|nine|ten)"
            r"(?:\s+to\s+(?:one|two|three|four|five|six|seven|eight|nine|ten))?"
            r"\s+years?(?:\s+of\s+experience)?)",
            text,
            re.IGNORECASE,
        )

        return list(set(matches))

    @staticmethod
    def extract_required_skills(text: str):

        found = set()
        lower_text = text.lower()

        for skill in SKILLS_DB:
            pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"

            if re.search(pattern, lower_text):
                found.add(skill)

        return sorted(found)

    @staticmethod
    def extract_preferred_skills(text: str):

        preferred_section_pattern = re.compile(
            r"(?:preferred|nice[\s\-]to[\s\-]have|bonus|good[\s\-]to[\s\-]have)\s*:?\s*\n"
            r"((?:.+\n?){1,20})",
            re.IGNORECASE,
        )

        inline_pattern = re.compile(
            r"(?:preferred|nice[\s\-]to[\s\-]have|bonus|good[\s\-]to[\s\-]have)\s*:?\s*(.+)",
            re.IGNORECASE,
        )

        preferred = []

        section_match = preferred_section_pattern.search(text)

        if section_match:
            for line in section_match.group(1).split("\n"):
                line = re.sub(r"^[\s\-\*\u2022]+", "", line).strip()

                if len(line) > 3:
                    preferred.append(line)

            return preferred

        for match in inline_pattern.finditer(text):
            line = match.group(1).strip()

            if len(line) > 3:
                preferred.append(line)

        return preferred

    @staticmethod
    def extract_responsibilities(text: str):

        section_pattern = re.compile(
            r"(?:responsibilities|what you(?:'ll| will) do|key\s+duties|your\s+role)\s*:?\s*\n"
            r"((?:.+\n?){1,30})",
            re.IGNORECASE,
        )

        bullet_pattern = re.compile(
            r"^[\s\-\*\u2022\d+\.\)]+",
            re.MULTILINE,
        )

        section_match = section_pattern.search(text)

        section_text = section_match.group(1) if section_match else text

        responsibilities = []

        for line in section_text.split("\n"):
            line = bullet_pattern.sub("", line).strip()

            if len(line) > 30:
                responsibilities.append(line)

        return responsibilities[:10]

    @staticmethod
    def extract_education_required(text: str):

        patterns = [
            "bachelor",
            "master",
            "mba",
            "phd",
            "doctorate",
            "associate",
            "b.tech",
            "m.tech",
            "b.e",
            "m.e",
            "b.sc",
            "m.sc",
            "degree",
            "diploma",
            "graduate",
            "computer science",
            "information technology",
            "engineering",
        ]

        results = []

        for line in text.split("\n"):
            lower = line.lower()

            if any(p in lower for p in patterns):
                cleaned = line.strip()

                if cleaned and cleaned not in results:
                    results.append(cleaned)

        return results

    @classmethod
    def extract(cls, jd_text: str) -> dict:

        return {
            "job_title": cls.extract_job_title(jd_text),
            "experience_required": cls.extract_experience_required(jd_text),
            "required_skills": cls.extract_required_skills(jd_text),
            "preferred_skills": cls.extract_preferred_skills(jd_text),
            "responsibilities": cls.extract_responsibilities(jd_text),
            "education_required": cls.extract_education_required(jd_text),
        }