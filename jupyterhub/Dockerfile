# ARG JUPYTERHUB_VERSION=0.9.2
ARG JUPYTERHUB_VERSION=latest
FROM jupyterhub/jupyterhub:${JUPYTERHUB_VERSION}
RUN pip install -U pip\
        dockerspawner \
        jupyterhub-dummyauthenticator \
        jupyterhub-ldapauthenticator
