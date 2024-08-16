# Inspired by https://dev.to/pencillr/test-ansible-playbooks-using-docker-ci0

FROM ubuntu:latest

ARG USER=ansibleuser

# Add sudo and openssh-server
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update -y \
  && apt install -y --no-install-recommends \
      openssh-server \
      sudo \
      # Actually needed by ansible
      python3

# Setup running user on the container with sudo rights and
# password-less ssh login
RUN useradd -m ${USER} && adduser ${USER} sudo && echo "${USER} ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/sudoers

# As the user setup the ssh identity using the key in the tmp folder
USER "${USER}"
RUN mkdir ~/.ssh && chmod -R 700 ~/.ssh
COPY --chown=${USER}:sudo id_rsa.pub /home/${USER}/.ssh/id_rsa.pub
RUN cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys && chmod 644 ~/.ssh/id_rsa.pub && chmod 644 ~/.ssh/authorized_keys

# start ssh with port exposed
USER root
RUN service ssh start

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D", "-e"]
