FROM marcpartensky/gpg

RUN apk update
RUN apk add cmake libssl-dev

WORKDIR /build
RUN git clone https://github.com/jiep/kyber-gake /build
RUN mkdir build
WORKDIR /build/build
RUN cmake -DCMAKE_BUILD_TYPE=Release ..
RUN make
