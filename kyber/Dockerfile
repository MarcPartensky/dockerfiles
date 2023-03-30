FROM marcpartensky/gpg

RUN apk add musl-dev gcc py3-pip
RUN apk add py3-pip
RUN pip install kyber-py
COPY gen /usr/bin

ENTRYPOINT ["python"]
