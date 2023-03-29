FROM alpine

ENV KEYS_PATH=/root/keys
ENV RECIPIENT=marc@marcpartensky.com
ENV KEYRING=8E097DDB13F0722F

RUN apk add gpg gpg-agent p7zip
COPY encrypt /usr/bin/encrypt
COPY entrypoint.sh /root/entrypoint.sh

COPY encryption.pub /
RUN gpg --import encryption.pub
RUN rm encryption.pub


ENTRYPOINT ["/root/entrypoint.sh"]
