#!/usr/bin/env bash

sleep 10

# without any warmup
nice -20 taskset 0x1 ./run_mmap.py --runtime=runc --iterations=100000
nice -20 taskset 0x1 ./run_mmap.py --runtime=runsc-kvm --iterations=100000

nice -20 taskset 0x1 ./run_mmap.py --runtime=runc --iterations=250000
nice -20 taskset 0x1 ./run_mmap.py --runtime=runsc-kvm --iterations=250000

nice -20 taskset 0x1 ./run_mmap.py --runtime=runc --iterations=500000
nice -20 taskset 0x1 ./run_mmap.py --runtime=runsc-kvm --iterations=500000

# with 100000 warmup iterations inside process
nice -20 taskset 0x1 ./run_mmap.py --runtime=runc --iterations=100000 --warmup=100000
nice -20 taskset 0x1 ./run_mmap.py --runtime=runsc-kvm --iterations=100000 --warmup=100000

nice -20 taskset 0x1 ./run_mmap.py --runtime=runc --iterations=250000 --warmup=100000
nice -20 taskset 0x1 ./run_mmap.py --runtime=runsc-kvm --iterations=250000 --warmup=100000

nice -20 taskset 0x1 ./run_mmap.py --runtime=runc --iterations=500000 --warmup=100000
nice -20 taskset 0x1 ./run_mmap.py --runtime=runsc-kvm --iterations=500000 --warmup=100000

# with 200000 warmup iterations inside process
nice -20 taskset 0x1 ./run_mmap.py --runtime=runc --iterations=100000 --warmup=200000
nice -20 taskset 0x1 ./run_mmap.py --runtime=runsc-kvm --iterations=100000 --warmup=200000

nice -20 taskset 0x1 ./run_mmap.py --runtime=runc --iterations=250000 --warmup=200000
nice -20 taskset 0x1 ./run_mmap.py --runtime=runsc-kvm --iterations=250000 --warmup=200000

nice -20 taskset 0x1 ./run_mmap.py --runtime=runc --iterations=500000 --warmup=200000
nice -20 taskset 0x1 ./run_mmap.py --runtime=runsc-kvm --iterations=500000 --warmup=200000

# with 2 warmup trails in one docker
nice -20 taskset 0x1 python3 run_mmap_warmuptrail.py --runtime=runc --iterations=100000
nice -20 taskset 0x1 python3 run_mmap_warmuptrail.py --runtime=runsc-kvm --iterations=100000

nice -20 taskset 0x1 python3 run_mmap_warmuptrail.py --runtime=runc --iterations=250000
nice -20 taskset 0x1 python3 run_mmap_warmuptrail.py --runtime=runsc-kvm --iterations=250000

nice -20 taskset 0x1 python3 run_mmap_warmuptrail.py --runtime=runc --iterations=500000
nice -20 taskset 0x1 python3 run_mmap_warmuptrail.py --runtime=runsc-kvm --iterations=500000

# with 5 warmup trails in one docker 
nice -20 taskset 0x1 python3 run_mmap_warmuptrail.py --runtime=runc --iterations=100000 --warmup=5
nice -20 taskset 0x1 python3 run_mmap_warmuptrail.py --runtime=runsc-kvm --iterations=100000 --warmup=5

nice -20 taskset 0x1 python3 run_mmap_warmuptrail.py --runtime=runc --iterations=250000 --warmup=5
nice -20 taskset 0x1 python3 run_mmap_warmuptrail.py --runtime=runsc-kvm --iterations=250000 --warmup=5

nice -20 taskset 0x1 python3 run_mmap_warmuptrail.py --runtime=runc --iterations=500000 --warmup=5
nice -20 taskset 0x1 python3 run_mmap_warmuptrail.py --runtime=runsc-kvm --iterations=500000 --warmup=5

