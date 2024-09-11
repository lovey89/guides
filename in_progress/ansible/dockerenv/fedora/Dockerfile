FROM fedora:latest

ARG USER=ansibleuser

RUN yum clean all \
  && yum update -y \
  && yum install -y \
      openssh-server \
      sudo

RUN useradd -m ${USER} && usermod -aG wheel ${USER} && echo "${USER} ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

# As the user setup the ssh identity using the key in the tmp folder
USER "${USER}"
RUN mkdir ~/.ssh && chmod -R 700 ~/.ssh
COPY --chown=${USER}:sudo id_rsa.pub /home/${USER}/.ssh/id_rsa.pub
RUN cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys && chmod 644 ~/.ssh/id_rsa.pub && chmod 644 ~/.ssh/authorized_keys

# start ssh with port exposed
USER root

RUN ssh-keygen -A

EXPOSE 22

# Old solution. With this one systemctl would not work
#CMD ["/usr/sbin/sshd","-D","-e"]

# New solution with working systemctl. Requires privileged to work
ENTRYPOINT ["/sbin/init"]
CMD ["/bin/sleep", "infinity"]