from .extractor import JDExtractor

class JDParserService:
    @staticmethod
    def parse_jd(jd_text: str) -> dict:
        if not jd_text or not jd_text.strip():
            raise ValueError("Job description text cannot be empty.")

        return JDExtractor.extract(jd_text)