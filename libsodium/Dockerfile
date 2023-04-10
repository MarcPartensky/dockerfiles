FROM node:10.16.0-alpine

# Install required packages for building libsodium
RUN apk update && \
    apk add --no-cache git build-base npm libtool autoconf automake

# RUN apk add --no-cache --virtual .build-deps alpine-sdk python
# RUN npm install --production --silent
# RUN apk del .build-deps
# RUN apk add --no-cache libtool
# RUN apk add --no-cache --virtual .build-deps alpine-sdk python
# RUN npm install --production --silent
# RUN apk del .build-deps
RUN npm install -g node-gyp-build
# RUN node-gyp-build "node preinstall.js" "node postinstall.js"

RUN npm install -g sodium-cli

# Download and compile libsodium
RUN git clone --branch stable https://github.com/jedisct1/libsodium.git && \
    cd libsodium && \
    ./autogen.sh && \
    ./configure --prefix=/usr && \
    make && \
    make install && \
    cd .. && \
    rm -rf libsodium

# Cleanup build dependencies
RUN apk del git build-base

# Verify that the sodium binary is installed and working
# RUN sodium --version
RUN keygen

CMD ["/bin/sh"]
