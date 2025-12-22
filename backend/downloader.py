import yt_dlp
import uuid
import os
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOWNLOAD_DIR = os.path.join(BASE_DIR, "downloads")

def download_audio(url):
    unique_id = uuid.uuid4().hex[:8]
    final_mp3 = os.path.join(DOWNLOAD_DIR, f"{unique_id}.mp3")

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(DOWNLOAD_DIR, f"{unique_id}.%(ext)s"),
        'ffmpeg_location': r'C:\ffmpeg\bin',
        'addmetadata': True,
        'writethumbnail': True,
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            },
            {'key': 'EmbedThumbnail'},
            {'key': 'FFmpegMetadata'}
        ],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.extract_info(url, download=True)

   
    for _ in range(30):  
        if os.path.exists(final_mp3):
            return f"{unique_id}.mp3"
        time.sleep(0.1)

    
    raise Exception("MP3 file was not created")
