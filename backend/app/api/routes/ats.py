from fastapi import APIRouter
from app.agents.agent3_ats_scoring.schemas import ATSRequest
from app.agents.agent3_ats_scoring.service import ATSService
router = APIRouter()
@router.post("/score")
def score_resume(request: ATSRequest):

    result = ATSService.score_resume(
        request.resume_data,
        request.jd_data
    )
    return {
        "success": True,
        "data": result
    }