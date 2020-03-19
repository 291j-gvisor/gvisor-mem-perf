#!/usr/bin/env python3
# Assuming Python 3.6

import os
import subprocess as sp
from argparse import ArgumentParser
from pathlib import Path

import docker

# Configurations
# https://github.com/EthanGYoung/gvisor_analysis/blob/master/configs/memory_config.sh
# CMDS = ['bin/malloc_free', 'bin/malloc_nofree']
# CMDS = ['bin/malloc_nofree_notouch']
MODE = ["notouch_nofree", "notouch_free", "touch_nofree", "touch_free"]
MAX_MEM = 512*1024*1024
MMAP_THRESHOLD = 128*1024
TRIALS = 10
ITERATIONS = 100000
MALLOC_SIZES = [1024 * 2**i for i in range(11)]  # B

# Global preparations
os.chdir(Path(__file__).parent)
docker_client = docker.from_env()
image, _ = docker_client.images.build(path='.')

def run(cmd, runtime='native'):
    if runtime == 'native':
        return run_native(cmd)
    else:
        return run_docker(cmd, runtime)

def run_native(cmd):
    cp = sp.run(cmd, shell=True, stdout=sp.PIPE)
    return cp.stdout.decode().strip()

def run_docker(cmd, runtime='runc'):
    stdout = docker_client.containers.run(image, command=cmd, runtime=runtime, remove=True)
    return stdout.decode().strip()

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--runtime', default='native')
    args = parser.parse_args()
    runtime = args.runtime

    for mode, modename in enumerate(MODE):
        out_file = Path(f'data/{runtime}/malloc_{modename}.csv')
        os.makedirs(out_file.parent, exist_ok=True)
        print(out_file)
        with out_file.open('w') as f:
            header_line = 'malloc_size,latency'
            print(header_line)
            f.write(f'{header_line}\n')
            for malloc_size in MALLOC_SIZES:
                iterations = MAX_MEM / malloc_size if (malloc_size * ITERATIONS > MAX_MEM) else ITERATIONS
                full_cmd = f'bin/malloc_benchmark {iterations} {malloc_size} {mode} {MMAP_THRESHOLD}' if runtime != 'runsc' else f'bin/malloc_benchmark {iterations} {malloc_size} {mode}'
                print(full_cmd)
                for trial in range(TRIALS):
                    stdout = run(full_cmd, runtime=runtime)
                    elapsed_time = stdout.strip()
                    data_line = f'{malloc_size},{elapsed_time}'
                    print(data_line)
                    f.write(f'{data_line}\n')
