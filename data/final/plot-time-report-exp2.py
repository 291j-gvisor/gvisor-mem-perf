#!/usr/bin/env python3
"""
Example:
$ ./plot-time-report-exp2.py path/to/time_exp2_anon
"""
from argparse import ArgumentParser
from pathlib import Path
from io import StringIO

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

THIS_DIR = Path(__file__).absolute().parent

def read_data(data_dir):
    df = pd.DataFrame()
    for data_file in sorted(data_dir.iterdir()):
        if not data_file.name.startswith('time_report'):
            continue
        size = int(data_file.name.split('_')[-1][:-1])
        df_file = read_data_file(data_file)
        df_file['size'] = size
        df = df.append(df_file)
    return df

def read_data_file(data_file, block_thresh=2):
    df = pd.DataFrame()
    in_block = False
    block_id = 1
    with data_file.open() as f:
        for line in f:
            if 'starts' in line:
                in_block = True
                block = ''
            elif 'ends' in line:
                in_block = False
                df_block = pd.read_csv(
                    StringIO(block),
                    names=['label', 'cycles'],
                    delim_whitespace=True,
                )
                df_block['block_id'] = block_id
                df_block['line_num'] = df_block.index + 1
                block_id += 1
                df = df.append(df_block)
            elif in_block:
                block += line
    df = df[df['block_id'] >= block_thresh]
    return df

# Parse arguments
parser = ArgumentParser()
parser.add_argument('data_dir', type=Path)
parser.add_argument('output', type=Path)
args = parser.parse_args()
data_dir = args.data_dir

df = read_data(data_dir)

sns.set(style='white', palette=['#70309F', '#4472C4', '#70AC47'])
ax = sns.pointplot(
    x=df['size'], y=df['cycles'], hue=df['label'], kind="point",
    ci=None, estimator=np.median
)
ax.set_title('Average cost of sub-functions vs. mmap size (fixed 50000 iterations)')
ax.set_xlabel('mmap size (KB)')
ax.set_ylabel('Cycles')
handles, _ = ax.get_legend_handles_labels()
ax.legend(handles, ["createVMALocked", "getPMAsLocked", "mapASLocked"])
plt.tight_layout()
plt.savefig(args.output)
