#!/usr/bin/env python3
# Assuming Python 3.6

import os
import subprocess as sp
from argparse import ArgumentParser
from pathlib import Path

import docker

# Configurations
# https://github.com/EthanGYoung/gvisor_analysis/blob/master/configs/memory_config.sh
CMDS = ['bin/mmap_private_nofree','bin/mmap_anon_nofree','bin/mmap_shared_nofree']

TRIALS = 10
ITERATIONSS = [100, 1000, 10000]
MMAP_SIZE = 1024 * 4

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
    stdout = docker_client.containers.run(image, command=cmd, runtime=runtime)
    return stdout.decode().strip()

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--runtime', default='native')
    args = parser.parse_args()
    runtime = args.runtime

    for cmd in CMDS:
        cmd_name = cmd.split('/')[-1]
        out_file = Path(f'data/{runtime}/{cmd_name}_scaling.csv')
        os.makedirs(out_file.parent, exist_ok=True)
        print(out_file)
        with out_file.open('w') as f:
            f.write('iterations,elapsed_time\n')
            for iterations in ITERATIONSS:
                for trial in range(TRIALS):
                    full_cmd = f'{cmd} {iterations} {MMAP_SIZE}'
                    stdout = run(full_cmd, runtime=runtime)
                    elapsed_time = stdout.strip()
                    line = f'{iterations},{elapsed_time}'
                    print(line)
                    f.write(f'{line}\n')
