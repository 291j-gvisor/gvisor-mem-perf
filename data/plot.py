#!/usr/bin/env python3
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

THIS_DIR = Path(__file__).parent

def get_bench_names(machine_dir):
    return ['malloc_free', 'malloc_nofree']

def make_plot(machine_dir, bench_name):
    df = pd.DataFrame()
    for runtime_dir in machine_dir.iterdir():
        if not runtime_dir.is_dir():
            continue
        df_ = pd.read_csv(runtime_dir / f'{bench_name}.csv')
        df_['runtime'] = runtime_dir.name
        df = df.append(df_)
    df['malloc_size_kb'] = df['malloc_size'] // 1024
    df['ops_per_sec'] = 1 / df['elapsed_time']
    sns.catplot(x="malloc_size_kb", y="ops_per_sec", hue="runtime", kind="bar", data=df)
    plt.savefig(machine_dir / f'{bench_name}.pdf')

for machine_dir in THIS_DIR.iterdir():
    if not machine_dir.is_dir():
        continue
    for bench_name in get_bench_names(machine_dir):
        make_plot(machine_dir, bench_name)
