#!/usr/bin/env python3
from argparse import ArgumentParser
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

THIS_DIR = Path(__file__).absolute().parent

def read_data(data_dir):
    df = pd.DataFrame()
    for free_or_not in ['nofree', 'free']:
        for runtime in ['native', 'runc', 'runsc-kvm']:
            for iterations in [100000, 250000, 500000]:
                base_dir = data_dir / f'{runtime}({iterations})'
                data_file = base_dir / f'mmap_anon_{free_or_not}.csv'
                if not data_file.exists():
                    continue
                df_ = pd.read_csv(data_file)
                df_['type'] = free_or_not
                df_['runtime'] = runtime
                df_['iterations'] = iterations
                df = df.append(df_)
    df['mmap_size_kb'] = df['mmap_size'] // 1024
    df['latency_ms'] = df['latency'] * 1e6
    return df

def plot_scaling_iter(df, data_dir, mmap_type):
    df = df[df['type'] == mmap_type]
    if len(df) == 0:
        return
    g = sns.catplot(
        x='iterations', y='latency_ms', hue='runtime', col='mmap_size_kb',
        data=df, kind='bar', ci=None,
    )
    g.set_axis_labels('Iterations', 'Latency (ms)')
    g.fig.suptitle(mmap_type)
    g.fig.subplots_adjust(top=.9)
    plt.savefig(data_dir / f'mmap_scaling_iter_{mmap_type}.pdf')

def plot_scaling_size(df, data_dir, mmap_type):
    df = df[df['type'] == mmap_type]
    if len(df) == 0:
        return
    g = sns.catplot(
        x='mmap_size_kb', y='latency_ms', hue='iterations', col='runtime',
        data=df, kind='bar', ci=None,
    )
    g.set_axis_labels('mmap Size (KB)', 'Latency (ms)')
    g.fig.suptitle(mmap_type)
    g.fig.subplots_adjust(top=.9)
    plt.savefig(data_dir / f'mmap_scaling_size_{mmap_type}.pdf')

# Parse arguments
parser = ArgumentParser()
parser.add_argument('data_dir', type=Path)
args = parser.parse_args()
data_dir = args.data_dir

df = read_data(data_dir)
plot_scaling_iter(df, data_dir, 'nofree')
plot_scaling_iter(df, data_dir, 'free')
plot_scaling_size(df, data_dir, 'nofree')
plot_scaling_size(df, data_dir, 'free')
