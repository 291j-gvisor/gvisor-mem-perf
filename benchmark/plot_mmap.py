#!/usr/bin/env python3
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

THIS_DIR = Path(__file__).parent

def get_bench_names(machine_dir):
    return ['mmap_private_nofree','mmap_anon_nofree','mmap_shared_nofree','mmap_private_free','mmap_anon_free','mmap_shared_free']

def make_plot(machine_dir, bench_name):
    df = pd.DataFrame()
    for runtime_dir in machine_dir.iterdir():
        if not runtime_dir.is_dir():
            continue
        df_ = pd.read_csv(runtime_dir / f'{bench_name}.csv')
        df_['runtime'] = runtime_dir.name
        df = df.append(df_)
    df['mmap_size_kb'] = df['mmap_size'] // 1024
    df['ops_per_sec'] = 1 / df['elapsed_time']
    sns.catplot(x="mmap_size_kb", y="ops_per_sec", hue="runtime", kind="bar", data=df)
    print("Printing to {}".format(machine_dir))
    plt.savefig(machine_dir / f'{bench_name}.pdf')

for machine_dir in THIS_DIR.iterdir():
    if not machine_dir.is_dir():
        continue
    for bench_name in get_bench_names(machine_dir):
        make_plot(machine_dir, bench_name)
