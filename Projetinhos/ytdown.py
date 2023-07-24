from pytube import  YouTube

link = input('URL: ')
yt = YouTube(link)
videos = yt.streams.all()
video = list(enumerate(videos))

for i in video:
    print(i)

dn_opt = int(input('Opção de download: '))
dn_video = videos[dn_opt]
try:
    dn_video.download()
except Exception as err:
    print(err)
finally:
    print('sucesso')




