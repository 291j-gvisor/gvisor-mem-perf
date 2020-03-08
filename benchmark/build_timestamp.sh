#!/bin/bash -x

CURDIR="$(dirname $(readlink -f $0))"

cd $CURDIR/../extern/gvisor-dev
bazel build runsc
sudo cp bazel-bin/runsc/linux_amd64_pure_stripped/runsc /usr/local/bin/runsc
sudo systemctl restart docker
cd $CURDIR
make
sudo docker image build . --tag gvisor-mem-perf
