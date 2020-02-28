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
#./run_mmap.py --iterations=50000
#./run_mmap.py --runtime=runc --iterations=50000
#./run_mmap.py --runtime=runsc-kvm --iterations=50000
#
./run_mmap.py --iterations=100000
./run_mmap.py --runtime=runc --iterations=100000
./run_mmap.py --runtime=runsc-kvm --iterations=100000

#./run_mmap.py --iterations=150000
#./run_mmap.py --runtime=runc --iterations=150000
#./run_mmap.py --runtime=runsc-kvm --iterations=150000

./run_mmap.py --iterations=250000
./run_mmap.py --runtime=runc --iterations=250000
./run_mmap.py --runtime=runsc-kvm --iterations=250000

./run_mmap.py --iterations=500000
./run_mmap.py --runtime=runc --iterations=500000
./run_mmap.py --runtime=runsc-kvm --iterations=500000

python3 run_mmap2.py --iterations=50000
python3 run_mmap2.py --runtime=runc --iterations=50000
python3 run_mmap2.py --runtime=runsc-kvm --iterations=50000

#./run_mmap_scaling.py
#./run_mmap_scaling.py --runtime=runc
#./run_mmap_scaling.py --runtime=runsc
#
#ls data
#ls data/native
