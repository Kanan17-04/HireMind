import re
class JDSectionExtractor:
    @staticmethod
    def extract(text: str) -> str:
        keywords = [
            "Job Details",
            "Apply",
            "About the job",
            "Minimum qualifications",
            "Qualifications",
            "Requirements",
            "Responsibilities",
            "What you'll do",
            "Preferred qualifications",
        ]

        positions = []
        lower_text = text.lower()
        for keyword in keywords:
            pos = lower_text.find(keyword.lower())
            if pos != -1:
                positions.append(pos)
        if positions:
            start = min(positions)
            extracted = text[start:]
            return extracted.strip()
        return text