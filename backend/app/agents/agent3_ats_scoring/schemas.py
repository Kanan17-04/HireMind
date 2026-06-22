from pydantic import BaseModel
class ATSRequest(BaseModel):
    resume_data: dict
    jd_data: dict
class ATSResponse(BaseModel):
    ats_score: float
    matching_skills: list[str]
    missing_skills: list[str]
    experience_match: bool
    education_match: bool