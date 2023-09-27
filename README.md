# spotwebdl
Web fork for spordl

This docker created a simple web interface to allow user spotdl directly from your brouser.

Ref to https://github.com/spotDL/spotify-downloader

## Run

docker run -d --name spotyweb -e PUID=1000 -e PGID=1000 -p [YOUR_PORT]:3344 -v [YOUR_LOCAL_MUSIC_PATH]:/music --restart=always spotyweb:0.0.1
