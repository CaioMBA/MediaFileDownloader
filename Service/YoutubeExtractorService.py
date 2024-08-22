import yt_dlp as youtube_dl
from Service.SystemService import System

class Youtube:
    def __init__(self):
        self.System = System()
        self.ydl_opts = {
            'format': 'best',
            'outtmpl': f'{self.System.DownloadsPath}/%(title)s.%(ext)s',
            'noplaylist': True
        }

    def Download(self, url: str, finalType: str = 'MP4'):
        with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            title = info_dict.get('title', 'video').replace('/', '_').replace('\\', '_')
            ext = info_dict.get('ext', 'mp4')
            download_path = fr"{self.System.DownloadsPath}\{title}.{ext}"
            ydl.params['outtmpl']['default'] = download_path
            ydl.download([url])

        if finalType.upper() == 'MP3':
            self.System.TransformMP4ToMP3(download_path)
        print('Download finalizado')