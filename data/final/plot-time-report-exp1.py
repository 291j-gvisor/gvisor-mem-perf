#!/usr/bin/env python3
from argparse import ArgumentParser
from pathlib import Path

import matplotlib.pyplot as plt
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
df_raw = pd.DataFrame()
for data_file in sorted(data_dir.iterdir()):
    if not data_file.name.startswith("time_report"):
        continue
    iterations = int(data_file.name.split("_")[-1])
    df_file = tb.read_time_report(data_file)
    df_file["iterations"] = iterations
    df_raw = df_raw.append(df_file)
df = pd.DataFrame()
for iterations in sorted(set(df_raw["iterations"])):
    df_iter = df_raw[df_raw["iterations"] == iterations][["line_num", "cycles"]]
    grp_median = df_iter.groupby("line_num").median()
    df_grp = pd.DataFrame(
        {
            "iteration": grp_median.index,
            "cycles": grp_median["cycles"],
            "group": iterations,
        }
    )
    df = df.append(df_grp)

# Make plot
sns.set(
    context="paper", style="white", font="serif", font_scale=0.8
)
plt.figure(figsize=(3.2, 2.4))
for group in sorted(set(df["group"])):
    df_iter = df[df["group"] == group]
    plt.plot(df_iter["iteration"], df_iter["cycles"], alpha=0.6, label=str(group))
plt.xlabel("Iteration")
plt.ylabel("Cycles")
plt.legend()
plt.tight_layout()
plt.savefig(args.output, dpi=400)
