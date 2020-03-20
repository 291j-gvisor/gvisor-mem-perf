from io import StringIO

import numpy as np
import pandas as pd


def read_exp(exp_dir):
    df = pd.DataFrame()
    for runtime_dir in sorted(exp_dir.iterdir()):
        if not runtime_dir.is_dir():
            continue
        if "(" in runtime_dir.name:
            runtime, iterations = runtime_dir.name.split("(")
            iterations = int(iterations[:-1])
        else:
            runtime = runtime_dir.name
            iterations = None
        for data_file in sorted(runtime_dir.iterdir()):
            if not data_file.is_file():
                continue
            operation = data_file.stem
            df_ = pd.read_csv(data_file)
            df_["runtime"] = runtime
            if iterations is not None:
                df_["iterations"] = iterations
            df_["operation"] = operation
            df = df.append(df_)
    df["latency_ms"] = df["latency"] * 1e6
    return df


def read_exp_malloc(exp_dir):
    df = read_exp(exp_dir)
    df["malloc_size_kb"] = df["malloc_size"] // 1024
    return df


def read_exp_mmap(exp_dir):
    df = read_exp(exp_dir)
    df["mmap_size_kb"] = df["mmap_size"] // 1024
    return df


def read_time_report(data_file, block_thresh=2):
    df = pd.DataFrame()
    in_block = False
    block_id = 1
    with data_file.open() as f:
        for line in f:
            if "starts" in line:
                in_block = True
                block = ""
            elif "ends" in line:
                in_block = False
                df_block = pd.read_csv(
                    StringIO(block), names=["label", "cycles"], delim_whitespace=True,
                )
                df_block["block_id"] = block_id
                df_block["line_num"] = df_block.index + 1
                block_id += 1
                df = df.append(df_block)
            elif in_block:
                block += line
    df = df[df["block_id"] >= block_thresh]
    return df


def show_values_on_bars(axs):
    def _show_on_single_plot(ax):
        for p in ax.patches:
            _x = p.get_x() + p.get_width() / 2
            _y = p.get_y() + p.get_height()
            value = "{:.1f}".format(p.get_height())
            ax.text(_x, _y, value, ha="center", fontsize=7)

    if isinstance(axs, np.ndarray):
        for idx, ax in np.ndenumerate(axs):
            _show_on_single_plot(ax)
    else:
        _show_on_single_plot(axs)
