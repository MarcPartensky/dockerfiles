FROM marcpartensky/gpg

RUN apk add musl-dev gcc py3-pip
RUN apk add py3-pip
RUN pip install kyber-py
COPY keygen enc dec /usr/bin/

ENTRYPOINT ["python"]
