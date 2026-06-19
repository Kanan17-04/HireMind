from pydantic import BaseModel
class JDRequest(BaseModel):
    jd_text: str | None = None
    jd_url: str | None = None
    file_path: str | None = None
class JDResponse(BaseModel):
    job_title: str
    experience_required: list[str]
    required_skills: list[str]
    preferred_skills: list[str]
    responsibilities: list[str]
    education_required: list[str]