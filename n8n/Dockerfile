FROM n8nio/n8n:latest

USER root
RUN apk update && apk add --no-cache docker-cli
RUN addgroup -g 116 docker && addgroup node docker

USER root
