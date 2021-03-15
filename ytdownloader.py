# first install:
# pip install pytube

import pytube

url = str(input("URL: "))
youtube = pytube.YouTube(url)
res = str(input("Resolution [(H)igh / (L)ow]: "))
while True:
    if res == "H":
        video = youtube.streams.get_highest_resolution()
        break
    elif res == "L":
        video = youtube.streams.first()
        break
    else:
        print("Wrong input!")
video.download()
print(video.title)