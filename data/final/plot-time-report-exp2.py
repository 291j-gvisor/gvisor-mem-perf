#!/usr/bin/env python3
from argparse import ArgumentParser
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

import toolbox as tb


# Parse arguments
parser = ArgumentParser()
parser.add_argument("data_dir", type=Path)
parser.add_argument("output", type=Path)
args = parser.parse_args()
data_dir = args.data_dir

# Read data
df = pd.DataFrame()
for data_file in sorted(data_dir.iterdir()):
    if not data_file.name.startswith("time_report"):
        continue
    size = int(data_file.name.split("_")[-1][:-1])
    df_file = tb.read_time_report(data_file)
    df_file["size"] = size
    df = df.append(df_file)

# Make plot
sns.set(
    context="paper", style="white", font="serif", font_scale=0.8
)
# sns.set(style='white', palette=['#70309F', '#4472C4', '#70AC47'])
plt.figure(figsize=(3.2, 2.4))
ax = sns.pointplot(
    x="size", y="cycles", hue="label", data=df, ci=None, estimator=np.median
)
ax.set_xlabel("mmap size (KB)")
ax.set_ylabel("Cycles")
handles, _ = ax.get_legend_handles_labels()
ax.legend(handles, ["createVMALocked", "getPMAsLocked", "mapASLocked"])
plt.tight_layout()
plt.savefig(args.output, dpi=400)
