FROM alpine
WORKDIR /root
RUN apk add hydra openssh
COPY entrypoint.sh /root/entrypoint.sh
ENTRYPOINT ["sh", "/root/entrypoint.sh"]
