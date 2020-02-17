#!/usr/bin/env bash

./run_all.py
./run_all.py --runtime=runc
./run_all.py --runtime=runsc

./run_all_mmap.py
./run_all_mmap.py --runtime=runc
./run_all_mmap.py --runtime=runsc

ls data
ls data/native
