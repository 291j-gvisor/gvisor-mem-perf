#!/usr/bin/env python3
"""
Example:
$ ./plot-time-report-exp1.py path/to/time_exp1_shared
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
        iterations = int(data_file.name.split('_')[-1])
        df_file = read_data_file(data_file)
        df_file['iterations'] = iterations
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
args = parser.parse_args()
data_dir = args.data_dir

df = read_data(data_dir)
for iterations in sorted(set(df['iterations'])):
    df_iter = df[df['iterations'] == iterations][['line_num', 'cycles']]
    grp = df_iter.groupby('line_num').median()
    plt.plot(grp.index, grp['cycles'], alpha=0.8, label=str(iterations))
plt.xlabel('iteration')
plt.ylabel('cycles')
plt.title('time report exp1')
plt.legend()
plt.savefig(data_dir / 'result.pdf')
