from fastapi import APIRouter, UploadFile, File, HTTPException
import os
import shutil
import subprocess

router = APIRouter()
UPLOAD_DIR = "rag/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/", tags=["Document Management"])
async def upload_file(file: UploadFile = File(...)):
    file_location = os.path.join(UPLOAD_DIR, file.filename)

    try:
        # Save file
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Run ingestion
        ingest_result = subprocess.run(
            ["python", "rag/ingest.py", file_location],
            capture_output=True,
            text=True
        )

        if ingest_result.returncode != 0:
            raise HTTPException(status_code=500, detail=f"Ingestion failed: {ingest_result.stderr}")

        return {
            "filename": file.filename,
            "message": "File uploaded and ingested successfully ✅"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))