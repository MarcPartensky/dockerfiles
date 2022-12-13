FROM sosedoff/pgweb:latest

RUN apt update
RUN apt install -y curl

HEALTHCHECK CMD curl localhost:8081
