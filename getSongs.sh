echo "Fetching song id's"
youtube-dl -j --flat-playlist "$1" | jq -r '.id' | sed 's_^_https://youtu.be/_' > .temp.txt
echo "Done Fetching song id's"
python3 .run.py