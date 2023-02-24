FROM python:alpine

RUN pip install yt-dlp
COPY entrypoint.sh /opt/entrypoint.sh

ENTRYPOINT ["/opt/entrypoint.sh"]
