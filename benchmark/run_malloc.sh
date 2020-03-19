#!/usr/bin/env bash

./run_malloc.py
./run_malloc.py --runtime=runc
./run_malloc.py --runtime=runsc
./run_malloc.py --runtime=runsc-kvm
