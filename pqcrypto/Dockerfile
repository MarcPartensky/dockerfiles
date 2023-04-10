FROM debian:stable-slim

# Install necessary packages
RUN apt-get update && \
    apt-get install -y build-essential libssl-dev libgmp-dev python3 wget && \
    rm -rf /var/lib/apt/lists/*

# Create libpqcrypto user
RUN adduser --disabled-password --gecos libpqcrypto libpqcrypto

# Switch to libpqcrypto user
USER libpqcrypto
WORKDIR /home/libpqcrypto

# Download and unpack libpqcrypto
RUN wget -m https://libpqcrypto.org/libpqcrypto-latest-version.txt
# ENV VERSION $(cat libpqcrypto.org/libpqcrypto-latest-version.txt)
ENV VERSION 20180314
RUN wget -m https://libpqcrypto.org/libpqcrypto-$VERSION.tar.gz
RUN tar -xzf libpqcrypto.org/libpqcrypto-$VERSION.tar.gz
WORKDIR libpqcrypto-$VERSION
RUN ln -s $HOME link-build
RUN ln -s $HOME link-install

# Compile and install libpqcrypto
RUN ./do

# Switch back to root user
USER root

# Cleanup
RUN rm -rf /home/libpqcrypto/libpqcrypto-$version && \
    rm -rf /home/libpqcrypto/libpqcrypto.org

CMD ["/bin/bash"]

# FROM alpine:3.15
#
# # Install build dependencies
# RUN apk add --no-cache build-base openssl-dev git cargo
#
# # Clone the pqcrypto repository
# RUN git clone https://github.com/rustpq/pqcrypto.git /usr/src/pqcrypto
#
# # Build the pqcrypto library and utilities
# WORKDIR /usr/src/pqcrypto
# RUN cargo build --release
#
# # Install the pqcrypto utilities
# RUN cp target/release/pqcrypto_* /usr/local/bin/
#
# # Clean up
# RUN apk del build-base && \
#     rm -rf /var/cache/apk/* /usr/src/*
#
# # Set the entrypoint to pqcrypto
# ENTRYPOINT ["pqcrypto"]

# # Use a multi-stage build to minimize final image size
# FROM rust:1.54-alpine3.14 AS builder
#
# # Install dependencies
# RUN apk --no-cache add build-base git make
#
# # Clone and build libpqcrypto
# RUN git clone https://github.com/PQClean/PQClean.git /tmp/PQClean && \
#     cd /tmp/PQClean/crypto_kem && \
#     make
#
# # Start with a fresh Alpine image
# FROM alpine:3.14
#
# # Copy the libpqcrypto binaries from the builder stage
# COPY --from=builder /tmp/PQClean/crypto_kem/bin/* /usr/local/bin/
#
# # Clean up unnecessary files from the final image
# RUN rm -rf /tmp/*
#
# # Set an entrypoint for the container
# ENTRYPOINT ["/bin/sh"]
#
