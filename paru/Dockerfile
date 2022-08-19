FROM archlinux:latest

RUN pacman -Syyyu --needed --noconfirm base-devel git
RUN useradd --create-home --groups wheel --shell /usr/bin/zsh marc
RUN passwd -d marc
RUN echo "%wheel ALL=(ALL) ALL" >> /etc/sudoers

USER marc
WORKDIR /tmp
RUN git clone https://aur.archlinux.org/paru.git
WORKDIR /tmp/paru
RUN makepkg -si --noconfirm
