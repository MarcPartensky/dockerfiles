FROM alpine

RUN apk add git
RUN adduser -D wallabag
USER wallabag
WORKDIR /home/wallabag
RUN git clone https://github.com/wallabag/wallabag.git .
USER root
RUN apk add git make bash composer
USER wallabag
RUN make install
RUN apk --purge del apk-tools
