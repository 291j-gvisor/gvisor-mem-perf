#!/usr/bin/env bash
# Check the versions of major tools in use.

gcc --version
bazel --version

go version
python --version
python3 --version

docker --version
runsc --version
runsc-dev --version
