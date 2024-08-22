import instaloader
import os
from facebook_scraper import get_posts
from Service.SystemService import System

class SocialMedia:
    def __init__(self):
        self.System = System()

    def downloadInstagramPost(self, url: str):
        shortCode: str = url.split('/')[-2]
        with instaloader.Instaloader() as instance:
            instance.download_post(instaloader.Post.from_shortcode(instance.context, shortCode), target=f'InstagramDownload')
        absoluteDownloadPath = os.path.abspath(f'InstagramDownload')
        self.System.moveFolder(absoluteDownloadPath)


    def downloadFaceBookPost(self, url: str):
        for post in get_posts(post_urls = [url]):
            if 'video' in post:
                self.System.RequestsDownload(post['video'], f"{self.System.DownloadsPath}/FacebookVideo.mp4")
            elif 'image' in post:
                self.System.RequestsDownload(post['image'], f"{self.System.DownloadsPath}/FacebookImage.png")
            else:
                print('Não foi possível baixar o post')
