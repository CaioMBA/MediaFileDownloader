import os,time,platform
from pytube import YouTube
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio

#Para compilar em um .EXE
#pyinstaller --onefile --icon=YoutubeDownload.ico main.py

def download_from_youtube(link='', output_type='mp4', output_path=os.path.join(os.path.expanduser("~"), "Downloads")):
    if link == '' or not link.__contains__('youtube'):
        clearConsole()
        print('Link inválido, por favor digite o link do vídeo do YOUTUBE!')
        time.sleep(2)
    try:
        clearConsole()
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        print('Iniciando Conexão ao Youtube')
        yt = YouTube(link)

        if output_type == 'mp4':
            yt_streams = yt.streams.filter(progressive=True,only_audio=False)
            Type = 'video'
            mimeType = 'video/mp4'
        elif output_type == 'mp3':
            yt_streams = yt.streams.filter(only_audio=True)
            Type = 'audio'
            mimeType = 'audio/mp4'

        print('=> Aqui estão as resoluções disponíveis!')
        QualityArray = []
        for i, stream in enumerate(yt_streams):
            if (stream.type == Type):
                print(f'[{i}] - Resolução:{stream.resolution} | Formato: {stream.mime_type} | Audio: {stream.abr}')
                QualityArray.append(i)
        yt_stream = yt_streams[get_user_quality_choice(QualityArray)]

        print('Iniciando Download do arquivo')
        yt_stream.download(output_path=output_path)

        if output_type == 'mp3':
            video_path = os.path.join(output_path, yt_stream.default_filename)
            ffmpeg_extract_audio(video_path, video_path.replace('mp4', 'mp3').replace('webm','mp3'))
            os.remove(video_path)

        print('Download finalizado')
    except Exception as e:
        print(f'Erro ao tentar fazer o download: {e}')

def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')
def get_user_type_choice():
    valid_types = ["mp3", "mp4"]
    while True:
        print('-------------------------------------------------------')
        print('Tipos válidos:')
        for output_type in valid_types:
            print(f'=> {output_type}')
        print('-------------------------------------------------------')
        output_type_choice = str(input('Digite o tipo de arquivo que deseja: '))
        if output_type_choice in valid_types:
            break
        print('Por favor, digite um valor válido')
        clearConsole()
    return output_type_choice
def get_user_quality_choice(Indexes = []):
    while True:
        print('-------------------------------------------------------')
        output_quality_choice = str(input('Digite o valor a esquerda da qualidade desejada: '))
        if int(output_quality_choice) in Indexes:
            break
        print('Por favor, digite um valor válido')
    return int(output_quality_choice)

if __name__ == '__main__':
    print('Iniciar Downloads from Youtube...')
    while True:
        output_type = get_user_type_choice()
        clearConsole()
        print('-------------------------------------------------------')
        print(f'Formato Escolhido:  {output_type}')
        print('-------------------------------------------------------')
        link = input('Digite o Link do vídeo do Youtube: ')
        download_from_youtube(link=link, output_type=output_type)
        print('-------------------------------------------------------')
        novamente = input('Digite [1] para continuar fazendo ou qualquer coisa para parar: ')
        if novamente != '1':
            break
        clearConsole()
