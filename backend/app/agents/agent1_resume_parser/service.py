from .parser import ResumeParser
from .extractor import ResumeExtractor
from .schemas import (
    ResumeSchema,
    ResumeResponseSchema,
)


class ResumeParserService:
    """
    Agent 1 Main Service

    Flow:

    Resume File
        ↓
    Parser
        ↓
    Raw Text
        ↓
    Extractor
        ↓
    Resume JSON
    """

    @staticmethod
    def process_resume(
        file_path: str,
    ) -> ResumeResponseSchema:

        try:

            raw_text = ResumeParser.parse(
                file_path
            )

            extracted_data = (
                ResumeExtractor.extract(
                    raw_text
                )
            )

            resume_data = ResumeSchema(
                name=extracted_data.get(
                    "name", ""
                ),
                email=extracted_data.get(
                    "email", ""
                ),
                phone=extracted_data.get(
                    "phone", ""
                ),
                skills=extracted_data.get(
                    "skills", []
                ),
                projects=extracted_data.get(
                    "projects", []
                ),
                experience=extracted_data.get(
                    "experience", []
                ),
                education=extracted_data.get(
                    "education", []
                ),
                certifications=extracted_data.get(
                    "certifications", []
                ),
                raw_text=raw_text,
            )

            return ResumeResponseSchema(
                success=True,
                message="Resume parsed successfully",
                data=resume_data,
            )

        except Exception as e:

            return ResumeResponseSchema(
                success=False,
                message=str(e),
                data=ResumeSchema(),
            )