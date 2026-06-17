from pathlib import Path
import shutil

from fastapi import (
    APIRouter,
    UploadFile,
    File,
    HTTPException,
)

from app.agents.agent1_resume_parser.service import (
    ResumeParserService,
)

router = APIRouter(
    prefix="/resume",
    tags=["Resume"],
)

UPLOAD_DIR = Path(
    "backend/app/storage/uploads"
)

UPLOAD_DIR.mkdir(
    parents=True,
    exist_ok=True,
)


@router.post("/upload")
async def upload_resume(
    file: UploadFile = File(...)
):
    try:

        file_path = (
            UPLOAD_DIR / file.filename
        )

        with open(
            file_path,
            "wb"
        ) as buffer:

            shutil.copyfileobj(
                file.file,
                buffer
            )

        result = (
            ResumeParserService.process_resume(
                str(file_path)
            )
        )

        return result.model_dump()

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )