# rkbx-dl

rkbx-dl is a lightweight wrapper around youtube-dl and FFmpeg to keep a rekordbox DJ music library syced with a youtube playlist. 

## Requirements 
A recent, working copy of [youtube-dl](https://github.com/ytdl-org/youtube-dl), [FFmpeg](https://ffmpeg.org) and [id3v2](https://id3v2.sourceforge.net) is needed.

## Installation

Clone the repo and navigate to the folder. 

## Use

Run 
```
./getSongs.sh PLAYLIST_URL
```
Where PLAYLIST_URL is the URL of a youtube playlist. The playlist must not be private (unlisted should work).

Once the script finishes, open Rekordbox-DJ navigate to `file>Import>Import Folder` and select the `songs` folder inside the repo. 

rkbx-dl will do its best to tag the songs it adds, but not every song will be perfect. Quickly check the added songs in rekordbox and make any changes as needed. 

__Note__: rekordbox will ignore songs which have been previously added, so you are able to keep all the new songs in the same `./songs` folder and rekordbox will diff them appropriately when importing the folder. 

## Suggestions

Add a `sync.command` file to the repo directory containing 
```
cd PATH_TO_DIR
.getSongs.sh PLAYLIST_URL
```
To sync your music library in the future, simply open the `sync.command` file from the finder and import the songs again in rekordbox. 





