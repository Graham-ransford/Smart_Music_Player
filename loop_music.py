import random, os
path="D:\MUSICS"
songs=os.listdir(path)
songs=[fi for fi in songs if fi.endswith(".mp3")]
print(songs)


