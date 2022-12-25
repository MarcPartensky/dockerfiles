FROM nixos/nix

WORKDIR /root
RUN git clone https://github.com/marcpartensky/dotfiles git/dotfiles
RUN mkdir -p /etc/nixos
RUN cp -r /root/git/dotfiles/nixos/.config/nixos/* /etc/nixos
RUN nixos-rebuild switch
