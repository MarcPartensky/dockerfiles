FROM python:alpine

RUN apk add git
RUN git clone https://github.com/sqlmapproject/sqlmap
WORKDIR sqlmap
ENTRYPOINT ["python", "sqlmap.py"]
