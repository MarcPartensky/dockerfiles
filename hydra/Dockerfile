FROM alpine
WORKDIR /root
RUN apk add hydra
COPY entrypoint.sh ./
ENTRYPOINT ["/root/entrypoint.sh"]
