#!/usr/bin/env bash

# Install general packages
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install -y \
    apt-transport-https \
    binutils-gold \
    build-essential \
    ca-certificates \
    clang-format \
    curl \
    git \
    gnupg-agent \
    software-properties-common

# Install Bazel
# https://docs.bazel.build/versions/master/install-ubuntu.html
curl https://bazel.build/bazel-release.pub.gpg | sudo apt-key add -
echo "deb [arch=amd64] https://storage.googleapis.com/bazel-apt stable jdk1.8" | sudo tee /etc/apt/sources.list.d/bazel.list
sudo apt-get update
sudo apt-get install -y bazel

# Install Python
sudo apt-get install -y \
    python \
    python3 \
    python3-pip

# Install Docker
# https://docs.docker.com/install/linux/docker-ce/ubuntu/
# https://docs.docker.com/install/linux/linux-postinstall/
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo apt-key fingerprint 0EBFCD88
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
sudo apt-get update
sudo apt-get install -y \
    docker-ce \
    docker-ce-cli \
    containerd.io
sudo groupadd docker
sudo usermod -aG docker $USER
# https://docker-py.readthedocs.io/
pip3 install docker

# Install gVisor
# https://github.com/google/gvisor#installing-from-source
# Since we need to modify gVisor source code in the future, let's install from source.
git clone https://github.com/google/gvisor.git gvisor
(
    cd gvisor
    bazel build runsc
    sudo cp ./bazel-bin/runsc/linux_amd64_pure_stripped/runsc /usr/local/bin
)

# Install KVM
# https://help.ubuntu.com/community/KVM/Installation
# We are using Ubuntu 10.04.
sudo apt-get install -y \
    qemu-kvm \
    libvirt-daemon-system \
    libvirt-clients \
    bridge-utils
sudo adduser `id -un` kvm
sudo adduser `id -un` libvirt

# Configure Docker
# https://gvisor.dev/docs/user_guide/quick_start/docker/#configuring-docker
cat << EOF | sudo tee /etc/docker/daemon.json
{
    "runtimes": {
        "runsc": {
            "path": "/usr/local/bin/runsc"
        },
        "runsc-kvm": {
            "path": "/usr/local/bin/runsc",
            "runtimeArgs": [
                "--platform=kvm"
            ]
        },
        "runsc-debug": {
            "path": "/usr/local/bin/runsc",
            "runtimeArgs": [
             		"--debug-log=/tmp/runsc",
                "--debug",
                "--strace"
            ]
        },
        "runsc-kvm-debug": {
            "path": "/usr/local/bin/runsc",
            "runtimeArgs": [
                "--platform=kvm",
            		"--debug-log=/tmp/runsc",
                "--debug",
                "--strace"
            ]
        }       
    }
}
EOF
sudo systemctl restart docker

# Clean up
sudo apt-get clean
