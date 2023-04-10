FROM python:alpine

LABEL maintainer="https://github.com/marcpartensky"

ENV TZ=Europe/Paris
ENV JUPYTER_ENABLE_LAB=yes
ENV PATH="$PATH:/home/jupyter/.local/bin"

RUN apk add --update sudo gcc g++ libc-dev linux-headers cargo nodejs

RUN addgroup -S jupyter && adduser -S jupyter -G jupyter
RUN passwd -d jupyter
USER jupyter

ENV HOME=/home/jupyter
WORKDIR $HOME

RUN pip install -U pip
RUN pip install \
        jupyterhub \
        jupyterlab \
        # jupyterlab-git \
        jupyterlab-lsp
        # jupyter-lsp-python \
        # jupyterlab-github

USER root
RUN apk --purge del cargo apk-tools

USER jupyter
RUN mkdir .jupyter
COPY jupyter_lab_config.py /home/jupyter/.jupyter/

ENTRYPOINT ["python", "-m", "jupyter", "lab"]
# ENTRYPOINT ["python", "-m", "jupyter", "lab", "--collaborative", "--ip 0.0.0.0 --no-browser --port=8080 --allow-root"]
# ENTRYPOINT ["jupyterhub-singleuser"]
# CMD ["jupyterhub-singleuser"]
