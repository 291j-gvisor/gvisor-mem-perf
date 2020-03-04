#!/usr/bin/env bash

sleep 10

# without any warmup
#./run_mmap.py --iterations=100000
#./run_mmap.py --runtime=runc --iterations=100000
#./run_mmap.py --runtime=runsc-kvm --iterations=100000

#./run_mmap.py --iterations=250000
#./run_mmap.py --runtime=runc --iterations=250000
#./run_mmap.py --runtime=runsc-kvm --iterations=250000
#
#./run_mmap.py --iterations=500000
#./run_mmap.py --runtime=runc --iterations=500000
#./run_mmap.py --runtime=runsc-kvm --iterations=500000

# with 100000 warmup iterations inside process
./run_mmap.py --runtime=runc --iterations=100000 --warmup=100000
./run_mmap.py --runtime=runsc-kvm --iterations=100000 --warmup=100000

./run_mmap.py --runtime=runc --iterations=250000 --warmup=100000
./run_mmap.py --runtime=runsc-kvm --iterations=250000 --warmup=100000

./run_mmap.py --runtime=runc --iterations=500000 --warmup=100000
./run_mmap.py --runtime=runsc-kvm --iterations=500000 --warmup=100000

# with 2 warmup trails in one docker
#python3 run_mmap_warmuptrail.py --runtime=runc --iterations=100000
#python3 run_mmap_warmuptrail.py --runtime=runsc-kvm --iterations=100000
#
#python3 run_mmap_warmuptrail.py --runtime=runc --iterations=250000
#python3 run_mmap_warmuptrail.py --runtime=runsc-kvm --iterations=250000
#
#python3 run_mmap_warmuptrail.py --runtime=runc --iterations=500000
#python3 run_mmap_warmuptrail.py --runtime=runsc-kvm --iterations=500000

