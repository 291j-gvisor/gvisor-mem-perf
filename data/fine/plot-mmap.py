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
        for runtime in ['native', 'runc', 'runsc']:
            for mmap_type in ['private', 'shared', 'anon']:
                base_dir = DATA_DIR / 'gcp-n1-standard-4' / runtime
                df_ = pd.read_csv(base_dir / f'mmap_{mmap_type}_{free_or_not}.csv')
                df_ = df_[df_['mmap_size'] == 1024 * 4]
                df_['label'] = f'{free_or_not}+{runtime}'
                df_['mmap_type'] = mmap_type
                df = df.append(df_)
    df['mmap_size_kb'] = df['mmap_size'] // 1024
    df['allocs_per_sec'] = 1 / df['elapsed_time']
    return df

def make_plot():
    df = read_data()
    fig, ax = plt.subplots(figsize=(3.5, 3))
    g = sns.catplot(
        x='mmap_type', y='allocs_per_sec', hue='label', data=df,
        kind='bar', ci=None, height=3.5, aspect=3.5/3.5, legend_out=False,
        log=True
    )
    (g
        .set_axis_labels('mmap Type', 'Operation Rate (Hz)')
        .set_xticklabels(['private', 'shared', 'anonymous'])
        .set(ylim=(1e3, 1e7))
    )
    h,l = g.axes[0][0].get_legend_handles_labels()
    g.axes[0][0].legend_.remove()
    g.fig.legend(h, l, ncol=2)
    g.fig.tight_layout()
    g.fig.subplots_adjust(top=0.75)

make_plot()
plt.savefig(f'mmap_log.pdf')
