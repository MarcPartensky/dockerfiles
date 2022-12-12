FROM python:alpine

LABEL maintainer="https://github.com/marcpartensky"

RUN apk add --update sudo gcc libc-dev linux-headers && rm -rf /var/cache/apk/*

RUN addgroup -S jupyter && adduser -S jupyter -G jupyter
RUN passwd -d jupyter
ENV HOME=/home/jupyter
WORKDIR $HOME
USER jupyter

ENV TZ=Europe/Paris
ENV JUPYTER_ENABLE_LAB=yes


RUN pip install -U pip\
        jupyterlab \
        jupyterlab-git \
        jupyterlab-lsp \
        # jupyter-lsp-python \
        jupyterlab-github

CMD ["jupyterhub-singleuser"]
