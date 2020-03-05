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

def read_data(data_dir, total_mem_gb=10):
    df = pd.DataFrame()
    for free_or_not in ['nofree', 'free']:
        for runtime in ['native', 'runc', 'runsc-kvm']:
            for iterations in [5000, 10000, 50000, 100000, 250000, 500000]:
                base_dir = data_dir / f'{runtime}({iterations})'
                if not base_dir.exists():
                    continue
                df_ = pd.read_csv(base_dir / f'mmap_anon_{free_or_not}.csv')
                df_['type'] = free_or_not
                df_['runtime'] = runtime
                df_['iterations'] = iterations
                df = df.append(df_)
    df['mmap_size_kb'] = df['mmap_size'] // 1024
    df['ops_per_sec'] = 1 / df['elapsed_time']
    # Exclude nofree data with total allocated mem > total mem
    if total_mem_gb is not None:
        df = df[
            (df['type'] == 'free') |
            (df['mmap_size_kb'] * df['iterations'] < total_mem_gb * 1024**2)
        ]
    return df

def plot_all_runtimes(df, tp, label=None):
    df = df[df['type'] == tp]
    g = sns.catplot(
        x='iterations', y='ops_per_sec', hue='runtime',
        col='mmap_size_kb', col_wrap=3,
        data=df, kind='bar', ci=None,
    )
    g.set_axis_labels('Iterations', 'Operations per Seconds')
    fn = f'mmap_scaling_{tp}'
    if label is not None:
        fn = f'{fn}_{label}'
    plt.savefig(f'{fn}.pdf')

def plot_runtime(df, runtime, label=None):
    df = df[df['runtime'] == runtime]
    g = sns.catplot(
        x='iterations', y='ops_per_sec', hue='mmap_size_kb', col='type',
        data=df, kind='bar', ci=None,
    )
    g.set_axis_labels('Iterations', 'Operations per Seconds')
    fn = f'mmap_scaling_{runtime}'
    if label is not None:
        fn = f'{fn}_{label}'
    plt.savefig(f'{fn}.pdf')

def plot_runtime_iterations(df, runtime, iterations, label=None):
    df = df[df['runtime'] == runtime]
    df = df[df['iterations'] == iterations]
    g = sns.catplot(
        x='mmap_size_kb', y='ops_per_sec', hue='type',
        data=df, kind='bar', ci=None,
    )
    g.set_axis_labels('mmap Size (kb)', 'Operations per second')
    fn = f'mmap_scaling_{runtime}_{iterations}'
    if label is not None:
        fn = f'{fn}_{label}'
    plt.savefig(f'{fn}.pdf')

df = read_data(DATA_DIR / 'linux')
plot_all_runtimes(df, 'free')
plot_all_runtimes(df, 'nofree')
plot_runtime(df, 'runsc-kvm')
plot_runtime(df, 'runc')

df = read_data(DATA_DIR / 'data1', total_mem_gb=None)
plot_runtime(df, 'native', label='data1')
plot_runtime(df, 'runc', label='data1')
plot_runtime(df, 'runsc-kvm', label='data1')

df = read_data(DATA_DIR / 'data2', total_mem_gb=None)
plot_runtime_iterations(df, 'runc', 50000, label='data2')
plot_runtime_iterations(df, 'runsc-kvm', 50000, label='data2')
