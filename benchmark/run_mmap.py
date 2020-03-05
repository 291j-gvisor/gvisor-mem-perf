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

TRIALS = 10
#WARMUP_IT = 100000
#ITERATIONS = 100000
MEM_LIMIT_G = 40
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
    stdout = docker_client.containers.run(image, command=cmd, runtime=runtime, remove=True, mem_limit=str(MEM_LIMIT_G+2)+'g')
    return stdout.decode().strip()

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--runtime', default='native')
    parser.add_argument('--iterations', default=100000)
    parser.add_argument('--warmup', default = 0)
    args = parser.parse_args()
    runtime = args.runtime
    ITERATIONS = int(args.iterations)
    WARMUP_IT = int(args.warmup)

    for cmd in CMDS:
        cmd_name = cmd.split('/')[-1]
        out_file = Path(f'exp1_withwarmupinsideprocess/{runtime}({ITERATIONS})/{cmd_name}.csv')
        os.makedirs(out_file.parent, exist_ok=True)
        print(out_file)
        with out_file.open('w') as f:
            f.write('mmap_size,latency\n')
            for mmap_size in MMAP_SIZES:
                iterations = MEM_LIMIT/mmap_size - WARMUP_IT if (ITERATIONS + WARMUP_IT) * mmap_size > MEM_LIMIT else ITERATIONS
                for trial in range(TRIALS):
                    full_cmd = f'{cmd} {iterations} {mmap_size} {WARMUP_IT}'
                    stdout = run(full_cmd, runtime=runtime)
                    elapsed_time = stdout.strip()
                    line = f'{mmap_size},{elapsed_time}'
                    print(line)
                    f.write(f'{line}\n')
