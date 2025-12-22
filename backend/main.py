from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from downloader import download_audio
import os

from downloader import download_audio
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOWNLOAD_DIR = os.path.join(BASE_DIR, "downloads")


@app.post("/convert")
def convert(Data: dict):
    
        url= Data.get("url")
        if not url:
            raise HTTPException(status_code=400, detail="URL is required")
        filename = download_audio(url)
        return {"status": "Download completed", "filename": filename}
    
    
@app.get("/download/{filename}")
def download_file(filename: str):
    file_path = os.path.join(DOWNLOAD_DIR, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(
        file_path,
        media_type="audio/mpeg",
        filename=filename
    )


        
   