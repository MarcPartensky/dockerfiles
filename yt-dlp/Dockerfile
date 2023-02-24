FROM python:alpine

RUN apk add ffmpeg
RUN pip install yt-dlp
COPY entrypoint.sh /opt/entrypoint.sh
WORKDIR /srv

ENTRYPOINT ["/opt/entrypoint.sh"]
