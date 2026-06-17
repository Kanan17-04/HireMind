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