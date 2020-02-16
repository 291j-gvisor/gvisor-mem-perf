#!/usr/bin/env bash
# Provision a work environment on a fresh Ubuntu OS.
# Ubuntu 18.04 LTS (Bionic Beaver) is assumed.
set -e

# Make sure this script is running in the project root dir
if [[ $PROJECT_ROOT ]]; then
    # Use the specified project root dir
    cd "$PROJECT_ROOT"
else
    # Determine project root dir automatically
    cd "$(dirname "$0")"
    cd ..
fi
pwd

# General preparation
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install -y \
    build-essential \
    clang-format \
    git
git submodule init
git submodule update

# Install Bazel
# https://docs.bazel.build/versions/master/install-ubuntu.html
sudo apt-get install -y curl
curl https://bazel.build/bazel-release.pub.gpg | sudo apt-key add -
echo "deb [arch=amd64] https://storage.googleapis.com/bazel-apt stable jdk1.8" | sudo tee /etc/apt/sources.list.d/bazel.list
sudo apt-get update
sudo apt-get install -y bazel

# Install Docker
# https://docs.docker.com/install/linux/docker-ce/ubuntu/
sudo apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common
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
# https://docs.docker.com/install/linux/linux-postinstall/
sudo groupadd -f docker
sudo usermod -aG docker "$USER"

# Install gVisor
# https://github.com/google/gvisor#installing-from-source
sudo apt-get install -y \
    git \
    bazel \
    python \
    python3 \
    python3-pip \
    docker-ce \
    build-essential \
    binutils-gold
for gvisor_version in 20200211 dev; do
(
    cd extern/gvisor-$gvisor_version
    bazel build runsc
    sudo cp ./bazel-bin/runsc/linux_amd64_pure_stripped/runsc /usr/local/bin/runsc-$gvisor_version
)
done

# Install KVM (experimental)
# https://help.ubuntu.com/community/KVM/Installation
sudo apt-get install -y \
    qemu-kvm \
    libvirt-daemon-system \
    libvirt-clients \
    bridge-utils
sudo adduser "$(id -un)" kvm
sudo adduser "$(id -un)" libvirt

# Configure Docker for gVisor
# https://gvisor.dev/docs/user_guide/quick_start/docker/#configuring-docker
cat << EOF | sudo tee /etc/docker/daemon.json
{
    "runtimes": {
        "runsc": {
            "path": "/usr/local/bin/runsc-20200211"
        },
        "runsc-kvm": {
            "path": "/usr/local/bin/runsc-20200211",
            "runtimeArgs": [
                "--platform=kvm"
            ]
        },
        "runsc-dev": {
            "path": "/usr/local/bin/runsc-dev"
        },
        "runsc-kvm-dev": {
            "path": "/usr/local/bin/runsc-dev",
            "runtimeArgs": [
                "--platform=kvm",
            ]
        }
        "runsc-debug": {
            "path": "/usr/local/bin/runsc"
            "runtimeArgs": [
             		"--debug-log=/tmp/runsc/",
                "--debug",
                "--strace"
            ]
        }
        "runsc-kvm-debug": {
            "path": "/usr/local/bin/runsc",
            "runtimeArgs": [
                "--platform=kvm",
            		"--debug-log=/tmp/runsc/",
                "--debug",
                "--strace"
            ]
        }       
    }
}
EOF
sudo systemctl restart docker

# Install required Python packages
pip3 install -r requirements.txt

# Finish up
sudo apt-get clean
