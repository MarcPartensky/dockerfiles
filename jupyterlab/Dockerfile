FROM python:alpine

LABEL maintainer="https://github.com/marcpartensky"

ENV TZ=Europe/Paris
ENV JUPYTER_ENABLE_LAB=yes
ENV PATH="${PATH}:/home/jupyter/.local"

RUN apk add --update sudo gcc libc-dev linux-headers cargo
RUN rm -rf /var/cache/apk/*

RUN addgroup -S jupyter && adduser -S jupyter -G jupyter
RUN passwd -d jupyter
ENV HOME=/home/jupyter
WORKDIR $HOME
USER jupyter

RUN pip install -U pip
RUN pip install \
        jupyterlab \
        jupyterlab-git \
        jupyterlab-lsp \
        # jupyter-lsp-python \
        jupyterlab-github

# CMD ["jupyterhub-singleuser"]
CMD ["python", "-m", "jupyterlab"]
