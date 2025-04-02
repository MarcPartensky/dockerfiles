FROM nixos/nix

WORKDIR /usr/local/waifu2x
RUN nix-env -i waifu2x-converter-cpp python3
COPY waifu2x.py /root/.nix-profile/bin/waifu2x

CMD ["waifu2x"]
