import os 
from datetime import datetime
import yt_dlp as youtube_dl
from subprocess import call 

print("Diffing new songs")

newSongs = open('.temp.txt', 'r')
newSong_lines = newSongs.readlines()

oldSongs = open('songs.txt', 'r')
oldSong_lines = oldSongs.readlines()

songsToAdd = []

for newSong in newSong_lines:
	if newSong not in oldSong_lines:
		songsToAdd.append(newSong)

print("Done diffing new songs")

os.chdir("songs")

print(f'Adding {len(songsToAdd)} songs')
for song in songsToAdd:
	ydl_opts = {
	    'format': 'bestaudio/best',
		'outtmpl': '%(id)s.%(ext)s',
	    'postprocessors': [{
	        'key': 'FFmpegExtractAudio',
	        'preferredcodec': 'mp3',
	        'preferredquality': '192',
	    }],
	}

	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		info_dict = ydl.extract_info(song, download=False)

		track = ""
		if 'track' in info_dict.keys():
			track = info_dict['track']

		artist = ""
		if 'artist' in info_dict.keys():
			artist = info_dict['artist']

		album = ""
		if 'album' in info_dict.keys():
			album = info_dict['album']

		title = ""
		if 'title' in info_dict.keys():
			title = info_dict['title']

		id = info_dict['id']

		ydl.download([song])

		goodTitle = title
		if artist != "" and track != "":
			goodTitle = f'{track}'
		
		os.rename(f'{id}.mp3', f'{goodTitle}.mp3')
		os.system(f'id3v2 --TIT2 "{goodTitle}" "{goodTitle}.mp3"')
		os.system(f'id3v2 --TPE1 "{artist}" "{goodTitle}.mp3"')
		os.system(f'echo "{song}" >>  ../songs.txt')

os.chdir("..")
os.remove(".temp.txt")

print("Done")

		




