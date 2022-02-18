#pip install pytube
from pytube import YouTube
link = input("Link: ")
video = YouTube(link)
stream = video.streams.get_highest_resolution()



#Ruta para guardar el vídeo
stream.download(r'C:\Users\desar\Documents')