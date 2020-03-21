#!/usr/bin/env python3
from argparse import ArgumentParser
from pathlib import Path

import seaborn as sns

import toolbox as tb


# Parse arguments
parser = ArgumentParser()
parser.add_argument("data_dir", type=Path)
parser.add_argument("output", type=Path)
parser.add_argument("--free", action="store_true")
args = parser.parse_args()
data_dir = args.data_dir

# Read data
df = tb.read_exp_malloc(data_dir)
df = df[df["malloc_size_kb"] > 2]
df["ops_per_sec"] = 1 / df["latency"]
df["label"] = ""
df["free"] = True
for i in range(len(df)):
    _, touch_or_not, free_or_not = df["operation"].iloc[i].split("_")
    if free_or_not == "nofree":
        df["free"].iloc[i] = False
    runtime = df["runtime"].iloc[i]
    df["label"].iloc[i] = f"{touch_or_not}+{runtime}"
# only keep nofree
if args.free:
    df = df[df["free"]]
else:
    df = df[~df["free"]]
df.sort_values(by=["operation", "runtime"], inplace=True)

# Make plot
sns.set(context="paper", style="white", font="serif", font_scale=0.8)
g = sns.catplot(
    x="malloc_size_kb",
    y="ops_per_sec",
    hue="label",
    data=df,
    kind="bar",
    ci=None,
    height=2.4,
    aspect=4 / 3,
    legend_out=False,
)
g.set_axis_labels("malloc size (KB)", "Operations per second")
g.axes[0][0].ticklabel_format(style="sci", axis="y", scilimits=(0, 1))
h, l = g.axes[0][0].get_legend_handles_labels()
g.axes[0][0].legend_.remove()
g.fig.legend(h, l, ncol=2)
g.fig.tight_layout()
g.fig.subplots_adjust(top=0.65)
g.savefig(args.output, dpi=400)
