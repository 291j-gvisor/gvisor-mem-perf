#!/usr/bin/env python3
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set(
    context='paper',
    style='white',
    font='serif',
)

THIS_DIR = Path(__file__).absolute().parent
DATA_DIR = THIS_DIR.parent

def read_data(free_or_not):
    df = pd.DataFrame()
    for touch_or_not in ['notouch', 'touch']:
        for runtime in ['native', 'runc', 'runsc']:
            base_dir = DATA_DIR / 'gcp-n1-standard-4' / runtime
            df_ = pd.read_csv(base_dir / f'malloc_{touch_or_not}_{free_or_not}.csv')
            df_['label'] = f'{touch_or_not}+{runtime}'
            df = df.append(df_)
    df['malloc_size_kb'] = df['malloc_size'] // 1024
    df['ops_per_sec'] = 1 / df['elapsed_time']
    return df

def make_plot(free_or_not):
    df = read_data(free_or_not)
    g = sns.catplot(
        x='malloc_size_kb', y='ops_per_sec', hue='label', data=df,
        kind='bar', ci=None, height=3.5, aspect=3.5/3.5, legend_out=False
    )
    (g
        .set_axis_labels('malloc size (KB)', 'Operations per second')
        # .set_xticklabels(['private', 'shared', 'anonymous'])
        # .set(ylim=(1e3, 1e7))
    )
    g.axes[0][0].ticklabel_format(style='sci', axis='y', scilimits=(0, 1))
    h,l = g.axes[0][0].get_legend_handles_labels()
    g.axes[0][0].legend_.remove()
    g.fig.legend(h, l, ncol=2)
    g.fig.tight_layout()
    g.fig.subplots_adjust(top=0.75)

for free_or_not in ['free', 'nofree']:
    make_plot(free_or_not)
    plt.savefig(f'malloc_{free_or_not}.png', dpi=400)
