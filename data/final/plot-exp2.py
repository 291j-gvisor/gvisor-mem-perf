#!/usr/bin/env python3
from argparse import ArgumentParser
from pathlib import Path

import seaborn as sns

import toolbox as tb


# Parse arguments
parser = ArgumentParser()
parser.add_argument("data_dir", type=Path)
parser.add_argument("output", type=Path)
args = parser.parse_args()
data_dir = args.data_dir

# Read data
df = tb.read_exp_mmap(data_dir)
df = df[df["mmap_size_kb"].isin([1, 64, 128, 256, 512, 1024])]

df1 = df[df['runtime'] == 'runc']
if 'anon' in data_dir.name:
    df2 = df[(df['runtime'] != 'runc') & (df['iterations'] == 25000)]
    df = df1.append(df2)

df = df.append({"mmap_size_kb": 3}, ignore_index=True)
df["mmap_size_kb"] = df["mmap_size_kb"].astype(int)
operation = df["operation"].iloc[0]

# Make plot
sns.set(context="paper", style="white", font="serif", font_scale=0.8)
g = sns.catplot(
    x="mmap_size_kb",
    y="latency_ms",
    hue="runtime",
    data=df,
    kind="bar",
    ci=None,
    height=1.6,
    aspect=4 / 2,
    legend_out=False,
)
tb.show_values_on_bars(g.axes)
g.set_axis_labels("mmap size (KB)", "Latency (ms)")
g.set_xticklabels([1, "...", 64, 128, 256, 512, 1024])
h, l = g.axes[0][0].get_legend_handles_labels()
g.axes[0][0].legend_.remove()
g.fig.legend(h, l, ncol=3)
g.fig.tight_layout()
g.fig.subplots_adjust(top=0.85)
g.savefig(args.output, dpi=400)
