#!/usr/bin/env python3
# Assuming Python 3.6

import os
import subprocess as sp
from argparse import ArgumentParser
from pathlib import Path

import docker

# Configurations
# https://github.com/EthanGYoung/gvisor_analysis/blob/master/configs/memory_config.sh
#CMDS = ['bin/mmap_private_nofree','bin/mmap_anon_nofree','bin/mmap_shared_nofree','bin/mmap_private_free','bin/mmap_anon_free','bin/mmap_shared_free']
CMDS = ['bin/mmap_anon_nofree']

WARMUP_TRIAL = 2
WARMUP_IT = -1
TRIALS = 10
#ITERATIONS = 100000
MEM_LIMIT_G = 50
MEM_LIMIT = 1024*1024*1024*MEM_LIMIT_G
MMAP_SIZES = [
    1024 * 4,
    1024 * 16,
    1024 * 64,
#    1024 * 256,
#    1024 * 1024,
]

# Global preparations
os.chdir(Path(__file__).parent)
docker_client = docker.from_env()
image, _ = docker_client.images.build(path='.', tag='mmap_test')

def run(cmd, runtime='native'):
    return run_docker(cmd, runtime)

def run_docker(cmd, runtime='runc'):
    realcmd = '/bin/bash -c "'+cmd
    for i in range(TRIALS+WARMUP_TRIAL-1):
        realcmd += '; ' + cmd
    realcmd+='"'
#    print(realcmd)
    stdout = docker_client.containers.run(image, command=realcmd, runtime=runtime, remove=True, mem_limit=str(MEM_LIMIT_G+2)+'g')
    return stdout.decode().strip()

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--runtime', default='runc')
    parser.add_argument('--iterations', default=100000)
    parser.add_argument('--warmuptrail', default=2)
    parser.add_argument('--warmupiteration', default=-1)
    args = parser.parse_args()
    runtime = args.runtime
    ITERATIONS = int(args.iterations)
    WARMUP_TRIAL = int(args.warmuptrail)
    WARMUP_IT = int(args.warmupiteration)

    for cmd in CMDS:
        cmd_name = cmd.split('/')[-1]
        if WARMUP_IT == -1: 
            out_file = Path(f'exp1_warmup_{WARMUP_TRIAL}_adaptive/{runtime}({ITERATIONS})/{cmd_name}.csv')
        else:
            out_file = Path(f'exp1_warmup_{WARMUP_TRIAL}_{WARMUP_IT}/{runtime}({ITERATIONS})/{cmd_name}.csv')
        os.makedirs(out_file.parent, exist_ok=True)
        print(out_file)
        with out_file.open('w') as f:
            f.write('mmap_size,latency\n')
            for mmap_size in MMAP_SIZES:
                iterations = MEM_LIMIT/mmap_size if ITERATIONS * mmap_size > MEM_LIMIT else ITERATIONS 
                full_cmd = f'{cmd} {iterations} {mmap_size}' if WARMUP_IT == -1 else f'{cmd} {iterations} {mmap_size} {WARMUP_IT}'
                stdout = run(full_cmd, runtime=runtime)
                elapsed_time = stdout.split('\n')
                for i in range(WARMUP_TRIAL,TRIALS+WARMUP_TRIAL-1):
                    line = f'{mmap_size},{elapsed_time[i]}'
                    print(line)
                    f.write(f'{line}\n')
