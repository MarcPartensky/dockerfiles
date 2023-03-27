FROM python:alpine

LABEL maintainer="https://github.com/marcpartensky"

ENV TZ=Europe/Paris
ENV JUPYTER_ENABLE_LAB=yes
ENV PATH="$PATH:/home/jupyter/.local/bin"

RUN apk add --update sudo gcc libc-dev linux-headers cargo

RUN addgroup -S jupyter && adduser -S jupyter -G jupyter
RUN passwd -d jupyter
USER jupyter

ENV HOME=/home/jupyter
WORKDIR $HOME

RUN pip install -U pip
RUN pip install \
        jupyterhub \
        jupyterlab \
        jupyterlab-git \
        jupyterlab-lsp \
        # jupyter-lsp-python \
        jupyterlab-github

USER root
RUN apk --purge del cargo apk-tools

USER jupyter

CMD ["/sbin/python", "-m", "jupyterhub-singleuser"]
# CMD ["python", "-m", "jupyterlab"]
