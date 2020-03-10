#!/usr/bin/env python3
from argparse import ArgumentParser
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

THIS_DIR = Path(__file__).absolute().parent
iterations = 25000

def read_data(data_dir):
    df = pd.DataFrame()
    for runtime in ['runc', 'runsc-kvm']:
        base_dir = data_dir / f'{runtime}({iterations})'
        data_file = base_dir / f'mmap_anon_nofree.csv'
        if not data_file.exists():
            continue
        df_ = pd.read_csv(data_file)
        df_['runtime'] = runtime
        df_['iterations'] = iterations
        df = df.append(df_)
    df['mmap_size_kb'] = df['mmap_size'] // 1024
    df['latency_ms'] = df['latency'] * 1e6
    return df

def show_values_on_bars(axs):
    def _show_on_single_plot(ax):
        for p in ax.patches:
            _x = p.get_x() + p.get_width() / 2
            _y = p.get_y() + p.get_height()
            value = '{:.2f}'.format(p.get_height())
            ax.text(_x, _y, value, ha="center")

    if isinstance(axs, np.ndarray):
        for idx, ax in np.ndenumerate(axs):
            _show_on_single_plot(ax)
    else:
        _show_on_single_plot(axs)

def plot_scaling_size(df, data_dir, label):
    g = sns.catplot(
        x='mmap_size_kb', y='latency_ms', hue='iterations', col='runtime',
        data=df, kind='bar', ci=None,
    )
    show_values_on_bars(g.axes)
    g._legend.remove()
    g.set_axis_labels('mmap Size (KB)', 'Latency (ms)')
    g.fig.suptitle(f'mmap (private anonymous) nofree, {label}, {iterations} iterations')
    g.fig.subplots_adjust(top=.9)
    g.savefig(data_dir / f'mmap_scaling_size.pdf')

# Parse arguments
parser = ArgumentParser()
parser.add_argument('data_dir', type=Path)
args = parser.parse_args()
data_dir = args.data_dir

df = read_data(data_dir)
plot_scaling_size(df, data_dir, data_dir.name)
