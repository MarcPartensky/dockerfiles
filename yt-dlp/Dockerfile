FROM python:alpine

RUN pip install yt-dlp
COPY entrypoint.sh /opt/entrypoint.sh
WORKDIR /srv

ENTRYPOINT ["/opt/entrypoint.sh"]
