from pathlib import Path

from .ocr import (
    extract_text_from_pdf,
    extract_text_from_docx,
    extract_text_from_image,
)


class ResumeParser:
    """
    Agent 1 Parser

    Responsibilities:
    - Validate file existence
    - Detect file type
    - Route to correct extractor
    - Return raw resume text
    """

    SUPPORTED_EXTENSIONS = {
        ".pdf",
        ".docx",
        ".png",
        ".jpg",
        ".jpeg",
    }

    @classmethod
    def parse(cls, file_path: str) -> str:
        file = Path(file_path)

        if not file.exists():
            raise FileNotFoundError(
                f"Resume file not found: {file_path}"
            )

        extension = file.suffix.lower()

        if extension not in cls.SUPPORTED_EXTENSIONS:
            raise ValueError(
                f"Unsupported file type: {extension}"
            )

        if extension == ".pdf":
            text = extract_text_from_pdf(
                str(file)
            )

        elif extension == ".docx":
            text = extract_text_from_docx(
                str(file)
            )

        else:
            text = extract_text_from_image(
                str(file)
            )

        if not text or not text.strip():
            raise ValueError(
                "No text could be extracted from resume."
            )

        return text.strip()