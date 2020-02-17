# gVisor Memory Subsystem Performance Improvement (WIP)

This is a course project in progress.

## Environment Setup

Throughout the project, the target OS is assumed to be Ubuntu 18.04 LTS (Bionic Beaver). To prepare a fresh OS for following work, just do:
```console
./script/provision-ubuntu.sh
```

Then you could check the versions of major tools in use:
```console
./script/check-versions.sh
```

### Vagrant

gVisor only works on Linux. If your local OS is not Linux, you could use a virtual machine for local development. A `Vagrantfile` is provided to facilitate setting up the VM environment. Just do:
```console
$ vagrant up
```

This project directory is synced with `~/work` within the VM. To get to work:
```console
$ vagrant ssh
$ cd work
```

### GCP and AWS

The cloud environment is not so much different from a local one. Start a proper instance, clone this repository somewhere, run the provision script, and you shall be good to go.

## Benchmark Run

Once the environment is set up, we could move on to do benchmarks. Following operations are assumed to be invoked in the `benchmark` directory.

### Manual commands

First compile the source code:
```
$ make
```

The compiled binaries could be found in `bin`. To run a benchmark natively:
```
$ ./bin/malloc_benchmark 1000 1024 0
```

To move forward, we need to build a docker image:
```
$ docker image build . --tag gvisor-mem-perf
```

To run the same command in Docker:
```console
$ docker run gvisor-mem-perf ./bin/malloc_benchmark 1000 1024 0
```

To run the same command in Docker with gVisor:
```console
$ docker run --runtime=runsc gvisor-mem-perf ./bin/malloc_benchmark 1000 1024 0
```

Other runtimes are configured in [`daemon.json`](daemon.json). The usages of `*-debug` and `*-prof` runtimes are more advanced. The details could be found in [gVisor documentation on debugging](https://gvisor.dev/docs/user_guide/debugging/).

### Automation scripts

To run a whole suite of benchmarks:
```console
$ ./run_all_all.sh
```

## Data Analysis

In the previous step, the results are saved in `benchmark/data`. To persist the data for further analysis, we need to move that directory to be a subdirectory of `data`. The naming convention is `data/{machine_type}`. For example, `data/gcp-n1-standard-4` means results from a `n1-standard-4` instance on GCP.

Once the `data` directory is populated, we could visualize the results using a Python script:
```console
$ ./data/plot.py
```
