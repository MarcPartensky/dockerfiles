FROM marcpartensky/gpg

RUN apk add musl-dev gcc git py3-pip
RUN git clone https://github.com/jack4818/kyber-py.git /root/git/kyber
WORKDIR /root/git/kyber
RUN pip install -r requirements.txt
COPY gen /usr/bin

ENTRYPOINT ["python"]
