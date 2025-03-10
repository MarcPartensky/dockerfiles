FROM etherpad/etherpad:latest

USER root
RUN npm install -g pnpm

RUN pnpm install --no-save \
    ep_headings2 \
    ep_align \
    ep_padlist2 \
    ep_themes \
    ep_mathjax \
    ep_markdown

USER etherpad
