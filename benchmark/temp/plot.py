#!/usr/bin/env python3
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

THIS_DIR = Path(__file__).parent

def get_bench_names(machine_dir):
    bench_names = []
    for path in (machine_dir / 'native').iterdir():
        if path.is_file():
            bench_names.append(path.stem)
    return bench_names

def make_plot(machine_dir, bench_name):
    print(machine_dir, bench_name)
    df = pd.DataFrame()
    for runtime_dir in sorted(machine_dir.iterdir()):
        if not runtime_dir.is_dir():
            continue
        df_ = pd.read_csv(runtime_dir / f'{bench_name}.csv')
        df_['runtime'] = runtime_dir.name
        df = df.append(df_)
    if 'malloc_size' in df:
        x_label = 'malloc_size_kb'
        df[x_label] = df['malloc_size'] // 1024
    elif 'mmap_size' in df:
        x_label = 'mmap_size_kb'
        df[x_label] = df['mmap_size'] // 1024
    elif 'iterations' in df:
        x_label = 'iterations'
    y_label = 'ops_per_sec'
    df[y_label] = 1 / df['elapsed_time']
    sns.catplot(x=x_label, y=y_label, hue="runtime", kind="bar", data=df)
    plt.title(bench_name)
    plt.tight_layout()
    plt.savefig(machine_dir / f'{bench_name}.pdf')
    plt.close()

for machine_dir in THIS_DIR.iterdir():
    if not machine_dir.is_dir() or machine_dir.name == 'fine':
        continue
    for bench_name in get_bench_names(machine_dir):
        make_plot(machine_dir, bench_name)
