#!/usr/bin/env bash
sudo perf record -g -e cycles:HG -F 10000 runsc --platform=kvm run mmap_test
sudo perf script | ../FlameGraph/stackcollapse-perf.pl > out.perf-folded
../FlameGraph/flamegraph.pl out.perf-folded > ../rust-perf.svg

