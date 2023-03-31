FROM alpine

RUN apk add git
WORKDIR /root/git/wallabag
RUN git clone https://github.com/wallabag/wallabag.git .
RUN apk add git make bash
# RUN make install
# RUN apk --purge del apk-tools
