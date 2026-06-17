from typing import List

from pydantic import BaseModel


class ResumeSchema(BaseModel):

    name: str = ""

    email: str = ""

    phone: str = ""

    skills: List[str] = []

    projects: List[str] = []

    experience: List[str] = []

    education: List[str] = []

    certifications: List[str] = []

    raw_text: str = ""


class ResumeResponseSchema(BaseModel):

    success: bool

    message: str

    data: ResumeSchema