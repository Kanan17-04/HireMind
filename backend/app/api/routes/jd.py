from fastapi import APIRouter, UploadFile, File, Form, HTTPException
import tempfile
import os
from app.agents.agent2_jd_parser.parser import JDParserService
router = APIRouter()
@router.post("/parse-jd")
def parse_jd(
    jd_text: str | None = Form(None),
    jd_url: str | None = Form(None),
    file: UploadFile | None = File(None)
):
    provided = sum([
        bool(jd_text),
        bool(jd_url),
        file is not None
    ])

    if provided != 1:
        raise HTTPException(
            status_code=400,
            detail="Provide exactly one of jd_text, jd_url, or file"
        )
    try:
        if jd_text:
            data = JDParserService.parse_jd(jd_text)
        elif jd_url:
            data = JDParserService.parse_jd_from_url(jd_url)
        else:
            suffix = os.path.splitext(file.filename)[1]
            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=suffix
            ) as tmp:
                tmp.write(file.read())
                temp_path = tmp.name
            data = JDParserService.parse_jd_from_file(
                temp_path
            )
            os.remove(temp_path)
        return {
            "success": True,
            "data": data
        }
    except Exception as e:
        return {
            "success": False,
            "message": str(e)
        }