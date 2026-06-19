# backend/app/agents/agent2_jd_parser/parser.py

from .extractor import JDExtractor
from .url_processor import URLProcessor
from .file_processor import FileProcessor
from .image_processor import ImageProcessor


class JDParserService:

    @staticmethod
    def parse_jd(jd_text: str) -> dict:
        """
        Parse raw JD text.
        """
        if not jd_text or not jd_text.strip():
            raise ValueError("Job description text cannot be empty.")

        return JDExtractor.extract(jd_text)

    @staticmethod
    def parse_jd_from_url(url: str) -> dict:
        jd_text = URLProcessor.extract_text(url)
        return JDExtractor.extract(jd_text)

    @staticmethod
    def parse_jd_from_pdf(file_path: str):

        text = FileProcessor.pdf_to_text(
            file_path
        )

        return JDExtractor.extract(text)

    @staticmethod
    def parse_jd_from_docx(file_path: str):

        text = FileProcessor.docx_to_text(
            file_path
        )

        return JDExtractor.extract(text)
    @staticmethod
    def parse_jd_from_image(file_path: str):

        text = ImageProcessor.image_to_text(
            file_path
        )
        return JDExtractor.extract(text)