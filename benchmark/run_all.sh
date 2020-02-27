#!/usr/bin/env bash

#./run_malloc.py
#./run_malloc.py --runtime=runc
#./run_malloc.py --runtime=runsc-kvm
#
#./run_mmap.py
#./run_mmap.py --runtime=runc
#./run_mmap.py --runtime=runsc-kvm
#
sleep 10
./run_mmap.py --iterations=50000
./run_mmap.py --runtime=runc --iterations=50000
./run_mmap.py --runtime=runsc-kvm --iterations=50000

./run_mmap.py --iterations=10000
./run_mmap.py --runtime=runc --iterations=10000
./run_mmap.py --runtime=runsc-kvm --iterations=10000

./run_mmap.py --iterations=5000
./run_mmap.py --runtime=runc --iterations=5000
./run_mmap.py --runtime=runsc-kvm --iterations=5000

#./run_mmap_scaling.py
#./run_mmap_scaling.py --runtime=runc
#./run_mmap_scaling.py --runtime=runsc
#
#ls data
#ls data/native
