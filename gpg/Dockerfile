FROM alpine

RUN apk add gpg gpg-agent p7zip
COPY entrypoint.sh /usr/bin/encrypt

COPY encryption.pub /
RUN gpg --import encryption.pub
RUN rm encryption.pub

ENTRYPOINT ["encrypt"]
