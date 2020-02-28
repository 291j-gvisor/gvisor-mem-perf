#!/usr/bin/env python3
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

sns.set(
    context='paper',
    style='white',
    font='serif',
)

THIS_DIR = Path(__file__).absolute().parent
DATA_DIR = THIS_DIR.parent

def read_data():
    df = pd.DataFrame()
    for free_or_not in ['nofree', 'free']:
        for runtime in ['native', 'runc', 'runsc-kvm']:
            for iterations in [5000, 10000, 50000, 100000]:
                base_dir = DATA_DIR / 'linux' / f'{runtime}({iterations})'
                df_ = pd.read_csv(base_dir / f'mmap_anon_{free_or_not}.csv')
                df_['type'] = free_or_not
                df_['runtime'] = runtime
                df_['iterations'] = iterations
                df = df.append(df_)
    df['mmap_size_kb'] = df['mmap_size'] // 1024
    df['ops_per_sec'] = 1 / df['elapsed_time']
    # Exclude nofree data with total allocated mem > 10GB
    df = df[
        (df['type'] == 'free') |
        (df['mmap_size_kb'] * df['iterations'] < 10 * 1024**2)
    ]
    return df

def plot_all_runtimes(df, tp):
    df = df[df['type'] == tp]
    g = sns.catplot(
        x='iterations', y='ops_per_sec', hue='runtime',
        col='mmap_size_kb', col_wrap=3,
        data=df, kind='bar', ci=None,
    )
    g.set_axis_labels('Iterations', 'Operations per Seconds')
    plt.savefig(f'mmap_scaling_{tp}.pdf')

def plot_kvm_only(df):
    df = df[df['runtime'] == 'runsc-kvm']
    g = sns.catplot(
        x='iterations', y='ops_per_sec', hue='mmap_size_kb', col='type',
        data=df, kind='bar', ci=None,
    )
    g.set_axis_labels('Iterations', 'Operations per Seconds')
    plt.savefig(f'mmap_scaling_kvm.pdf')

df = read_data()
plot_all_runtimes(df, 'free')
plot_all_runtimes(df, 'nofree')
plot_kvm_only(df)
