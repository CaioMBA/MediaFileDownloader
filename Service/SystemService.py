import os
import time
import platform
import subprocess
import requests
from tqdm import tqdm
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio

class System:
    def __init__(self):
        self.system = platform.system()
        self.DownloadsPath = os.path.join(os.path.expanduser("~"), "Downloads")

    @staticmethod
    def clearConsole():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def TransformMP4ToMP3(video_path: str):
        print(f'Tentando converter o arquivo: {video_path} para mp3')
        output_path = video_path.replace(".mp4", ".mp3").replace(".webm", ".mp3")
        time.sleep(1)
        try:
            ffmpeg_extract_audio(video_path, output_path)
            os.remove(video_path)
            print(f"Conversão concluída com sucesso! Salvo em: {output_path}")
        except subprocess.CalledProcessError as e:
            print(f"Um erro ocorreu durante a conversão: {e}")

    @staticmethod
    def RequestsDownload(url: str, outputPath: str):
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            total_length = int(r.headers.get('content-length'))
            with open(outputPath, 'wb') as f:
                with tqdm(total=total_length, unit='B', unit_scale=True, unit_divisor=1024) as bar:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)
                        bar.update(len(chunk))
        print(f"Download concluído: {outputPath}")

    @staticmethod
    def getDateTime():
        return time.strftime("%Y%m%d-%H%M%S")

    def moveFolder(self, folderPath: str):
        folderName:str = os.path.basename(folderPath)
        os.rename(folderPath, f"{self.DownloadsPath}\\{folderName}")