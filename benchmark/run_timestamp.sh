#!/bin/bash -x

if [ -z "$1" ]; then
    iter=1
else
    iter=$1
fi

if [ -z "$2" ]; then
    memsize=1
else
    memsize=$2
fi

sudo rm -rf /tmp/runs
sudo docker run --runtime=runsc-debug gvisor-mem-perf ./bin/mmap_anon_nofree $iter $memsize &>tmp
cat tmp | grep -A99999 -m1 -e 'START MMAP' | grep -A99999 -m1 -e "Mmap->MMap->Address Alignment" | grep -B99999 "END MMAP"
tail -n 1 tmp
