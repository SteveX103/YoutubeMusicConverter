import yt_dlp
def download_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'ffmpeg_location': r'C:\ffmpeg\bin',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
       
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl :
            ydl.download([url])