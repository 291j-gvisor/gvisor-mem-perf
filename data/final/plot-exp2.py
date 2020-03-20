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
df = df[df["mmap_size_kb"].isin([4, 16, 64, 256, 1024])]
operation = df["operation"].iloc[0]

# Make plot
sns.set(context="paper", style="white", font="serif", font_scale=1.5)
g = sns.catplot(
    x="mmap_size_kb",
    y="latency_ms",
    hue="runtime",
    data=df,
    kind="bar",
    ci=None,
    height=4.2,
    aspect=4 / 3,
    legend_out=False,
)
tb.show_values_on_bars(g.axes)
g.set_axis_labels("mmap size (KB)", "Latency (ms)")
h, l = g.axes[0][0].get_legend_handles_labels()
g.axes[0][0].legend_.remove()
g.fig.legend(h, l, ncol=3)
g.fig.tight_layout()
g.fig.subplots_adjust(top=0.9)
g.savefig(args.output, dpi=400)
