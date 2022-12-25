FROM nixos/nix

USER nixos
WORKDIR /home/nixos
RUN git clone https://github.com/marcpartensky/dotfiles ./git/dotfiles
RUN mkdir -p /etc/nixos
RUN cp -r ./git/dotfiles/nixos/.config/nixos/* /etc/nixos
RUN nixos-rebuild switch
