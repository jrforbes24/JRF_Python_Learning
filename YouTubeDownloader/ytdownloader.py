from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)



print("Title: ", yt.title)
print("Views: ", yt.views)

yd = yt.streams.get_by_resolution('720p')
yd.download(r'C:\Users\johnr\Videos\YoutubeDownloads')

print("Downloaded: ", yt.title, ".  From: ", argv[1])

