from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import HTTPException

from downloader import download_audio
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.post("/convert")
def convert(Data: dict):
    try:
        url= Data.get("url")
        if not url:
            raise HTTPException(status_code=400, detail="URL is required")
        download_audio(url)
        return{"status" : "Download completed"}
    except Exception as e:
        print("Error:",e)
        raise HTTPException(status_code=500, detail=str(e))

        
   