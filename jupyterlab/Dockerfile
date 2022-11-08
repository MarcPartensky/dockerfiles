FROM python:alpine

LABEL maintainer="https://github.com/marcpartensky"

ENV TZ=Europe/Paris
ENV JUPYTER_ENABLE_LAB=yes

RUN pip3 install \
    'jupyterhub==1.3.*' \
    'notebook==6.*'

RUN useradd -m jupyter
ENV HOME=/home/jupyter
WORKDIR $HOME
USER jupyter

RUN pip install -U pip\
        jupyterlab \
        jupyterlab-git \
        jupyterlab-lsp \
        jupyter-lsp-python \
        jupyterlab-github

CMD ["jupyterhub-singleuser"]
