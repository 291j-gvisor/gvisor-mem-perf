#!/usr/bin/env bash

sleep 10

# the selected one for anon
#nice -20 taskset 0x1 python3 run_mmap2.py --runtime=runc --iterations=25000
#nice -20 taskset 0x1 python3 run_mmap2.py --runtime=runsc-kvm --iterations=25000
nice -20 taskset 0x1 python3 run_mmap2.py --runtime=runsc-dev --iterations=50000

# the selected one for shared and private
#nice -20 taskset 0x1 python3 run_mmap2.py --runtime=runc --iterations=25000
#nice -20 taskset 0x1 python3 run_mmap2.py --runtime=runsc-kvm --iterations=25000

# for anon with timer
#nice -20 taskset 0x1 python3 run_mmap2.py --runtime=runsc-dev --iterations=50000

# without any warmup
#nice -20 taskset 0x1 ./run_mmap.py --runtime=runc --iterations=100000
#nice -20 taskset 0x1 ./run_mmap.py --runtime=runsc-kvm --iterations=100000
#
#nice -20 taskset 0x1 ./run_mmap.py --runtime=runc --iterations=250000
#nice -20 taskset 0x1 ./run_mmap.py --runtime=runsc-kvm --iterations=250000
#
#nice -20 taskset 0x1 ./run_mmap.py --runtime=runc --iterations=500000
#nice -20 taskset 0x1 ./run_mmap.py --runtime=runsc-kvm --iterations=500000

# with 100000 warmup iterations inside process
#nice -20 taskset 0x1 ./run_mmap.py --runtime=runc --iterations=100000
#nice -20 taskset 0x1 ./run_mmap.py --runtime=runsc-kvm --iterations=100000
#
#nice -20 taskset 0x1 ./run_mmap.py --runtime=runc --iterations=250000
#nice -20 taskset 0x1 ./run_mmap.py --runtime=runsc-kvm --iterations=250000
#
#nice -20 taskset 0x1 ./run_mmap.py --runtime=runc --iterations=500000
#nice -20 taskset 0x1 ./run_mmap.py --runtime=runsc-kvm --iterations=500000

# with 200000 warmup iterations inside process
#nice -20 taskset 0x1 ./run_mmap.py --runtime=runc --iterations=100000 --warmup=200000
#nice -20 taskset 0x1 ./run_mmap.py --runtime=runsc-kvm --iterations=100000 --warmup=200000
#
#nice -20 taskset 0x1 ./run_mmap.py --runtime=runc --iterations=250000 --warmup=200000
#nice -20 taskset 0x1 ./run_mmap.py --runtime=runsc-kvm --iterations=250000 --warmup=200000
#
#nice -20 taskset 0x1 ./run_mmap.py --runtime=runc --iterations=500000 --warmup=200000
#nice -20 taskset 0x1 ./run_mmap.py --runtime=runsc-kvm --iterations=500000 --warmup=200000

# with 2 warmup trails in one docker
#nice -20 taskset 0x1 python3 run_mmap_warmuptrail.py --runtime=runc --iterations=100000
#nice -20 taskset 0x1 python3 run_mmap_warmuptrail.py --runtime=runsc-kvm --iterations=100000
#
#nice -20 taskset 0x1 python3 run_mmap_warmuptrail.py --runtime=runc --iterations=250000
#nice -20 taskset 0x1 python3 run_mmap_warmuptrail.py --runtime=runsc-kvm --iterations=250000
#
#nice -20 taskset 0x1 python3 run_mmap_warmuptrail.py --runtime=runc --iterations=500000
#nice -20 taskset 0x1 python3 run_mmap_warmuptrail.py --runtime=runsc-kvm --iterations=500000

# with 5 warmup trails in one docker 
#nice -20 taskset 0x1 python3 run_mmap_warmuptrail.py --runtime=runc --iterations=100000 --warmuptrail=5
#nice -20 taskset 0x1 python3 run_mmap_warmuptrail.py --runtime=runsc-kvm --iterations=100000 --warmuptrail=5
#
#nice -20 taskset 0x1 python3 run_mmap_warmuptrail.py --runtime=runc --iterations=250000 --warmuptrail=5
#nice -20 taskset 0x1 python3 run_mmap_warmuptrail.py --runtime=runsc-kvm --iterations=250000 --warmuptrail=5
#
#nice -20 taskset 0x1 python3 run_mmap_warmuptrail.py --runtime=runc --iterations=500000 --warmuptrail=5
#nice -20 taskset 0x1 python3 run_mmap_warmuptrail.py --runtime=runsc-kvm --iterations=500000 --warmuptrail=5

# with 2 warmup trails in one docker and 100000 warmup iterations * 4096 inside process
#nice -20 taskset 0x1 python3 run_mmap_warmuptrail.py --runtime=runc --iterations=100000 --warmupiteration=100000
#nice -20 taskset 0x1 python3 run_mmap_warmuptrail.py --runtime=runsc-kvm --iterations=100000 --warmupiteration=100000
#
#nice -20 taskset 0x1 python3 run_mmap_warmuptrail.py --runtime=runc --iterations=250000 --warmupiteration=100000
#nice -20 taskset 0x1 python3 run_mmap_warmuptrail.py --runtime=runsc-kvm --iterations=250000 --warmupiteration=100000
#
#nice -20 taskset 0x1 python3 run_mmap_warmuptrail.py --runtime=runc --iterations=500000 --warmupiteration=100000
#nice -20 taskset 0x1 python3 run_mmap_warmuptrail.py --runtime=runsc-kvm --iterations=500000 --warmupiteration=100000

#
# with 2 warmup trails in one docker and 100000 warmup iterations inside process
#nice -20 taskset 0x1 python3 run_mmap_warmuptrail.py --runtime=runc --iterations=100000 --warmupiteration=100000 --warmuptrail=4
#nice -20 taskset 0x1 python3 run_mmap_warmuptrail.py --runtime=runsc-kvm --iterations=100000 --warmupiteration=100000 --warmuptrail=4
#
#nice -20 taskset 0x1 python3 run_mmap_warmuptrail.py --runtime=runc --iterations=250000 --warmupiteration=100000 --warmuptrail=4
#nice -20 taskset 0x1 python3 run_mmap_warmuptrail.py --runtime=runsc-kvm --iterations=250000 --warmupiteration=100000 --warmuptrail=4
#
#nice -20 taskset 0x1 python3 run_mmap_warmuptrail.py --runtime=runc --iterations=500000 --warmupiteration=100000 --warmuptrail=4
#nice -20 taskset 0x1 python3 run_mmap_warmuptrail.py --runtime=runsc-kvm --iterations=500000 --warmupiteration=100000 --warmuptrail=4
#
# with 2 warmup trails in one docker and 200000 warmup iterations inside process
#nice -20 taskset 0x1 python3 run_mmap_warmuptrail.py --runtime=runc --iterations=100000 --warmupiteration=200000
#nice -20 taskset 0x1 python3 run_mmap_warmuptrail.py --runtime=runsc-kvm --iterations=100000 --warmupiteration=200000
#
#nice -20 taskset 0x1 python3 run_mmap_warmuptrail.py --runtime=runc --iterations=250000 --warmupiteration=200000
#nice -20 taskset 0x1 python3 run_mmap_warmuptrail.py --runtime=runsc-kvm --iterations=250000 --warmupiteration=200000
#
#nice -20 taskset 0x1 python3 run_mmap_warmuptrail.py --runtime=runc --iterations=500000 --warmupiteration=200000
#nice -20 taskset 0x1 python3 run_mmap_warmuptrail.py --runtime=runsc-kvm --iterations=500000 --warmupiteration=200000
