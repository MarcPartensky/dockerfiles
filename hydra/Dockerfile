FROM alpine
WORKDIR /root
RUN apk add hydra
COPY entrypoint.sh /root/entrypoint.sh
ENTRYPOINT ["sh", "/root/entrypoint.sh"]
