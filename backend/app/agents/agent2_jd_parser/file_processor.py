# backend/app/agents/agent2_jd_parser/file_processor.py
import pdfplumber
import docx
class FileProcessor:
    @staticmethod
    def pdf_to_text(file_path: str) -> str:
        text = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text.strip()
    @staticmethod
    def docx_to_text(file_path: str) -> str:
        document = docx.Document(file_path)
        text = "\n".join(
            paragraph.text
            for paragraph in document.paragraphs
            if paragraph.text.strip()
        )
        return text.strip()