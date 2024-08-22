# Autor Caio Manoel
# Para compilar em um .EXE
# pyinstaller --onefile --uac-admin --icon=YoutubeDownload.ico main.py
from Service.SystemService import System
from Service.YoutubeExtractorService import Youtube
from Service.SocialMediaExtractorService import SocialMedia
import asyncio

class Main:
    def __init__(self):
        self.System = System()
        self.SocialMedia = SocialMedia()
        self.Youtube = Youtube()
        self.OutPutTypes: list[str] = ['mp4', 'mp3']
        while True:
            self.Menu()

    def Menu(self):
        print('1 - Baixar post do instagram')
        print('2 - Baixar post do facebook [ beta ]')
        print('3 - Baixar video do youtube')
        print('0 - Sair')
        option = input('Escolha uma opção: ')
        match option:
            case '1':
                self.SocialMedia.downloadInstagramPost(input('Digite a URL do post: '))
            case '2':
                self.SocialMedia.downloadFaceBookPost(input('Digite a URL do post: '))
            case '3':
                self.Youtube.Download(input('Digite a URL do video: '), self.ShowOutPutTypes())
            case '0':
                exit()
            case _:
                self.System.clearConsole()
                print('Opção inválida, tente novamente')

    def ShowOutPutTypes(self) -> str:
        while True:
            print('Escolha o tipo de arquivo')
            for index, outPutType in enumerate(self.OutPutTypes):
                print(f'[ {index} ] -> {outPutType.upper()}')
            option: int = input('Digite a opção: ')
            try:
                option = int(option)
            except:
                self.System.clearConsole()
                print('Opção inválida, tente novamente')
                continue
            if 0 <= option < len(self.OutPutTypes):
                return self.OutPutTypes[option]
            self.System.clearConsole()
            print('Opção inválida, tente novamente')



if __name__ == '__main__':
    Main()