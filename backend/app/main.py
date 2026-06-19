from fastapi import FastAPI

from app.api.routes.resume import (
    router as resume_router
)

app = FastAPI(
    title="HireMind API"
)

app.include_router(
    resume_router
)
from app.api.routes.jd import router as jd_router

app.include_router(
    jd_router,
    prefix="/api/jd",
    tags=["JD Parser"],
)