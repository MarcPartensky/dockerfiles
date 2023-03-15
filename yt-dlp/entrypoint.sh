#!/bin/sh

# default value
PLAYLIST_PATH=${PLAYLIST_PATH:-"/root/downloads/list.txt"}

while read playlist
do
    yt-dlp \
        -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio' \
        -ciw --audio-quality 0 \
        --embed-thumbnail \
        -o '%(title)s.%(ext)s' \
        --rm-cache-dir \
        $playlist
done < $PLAYLIST_PATH
