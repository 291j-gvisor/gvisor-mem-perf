#!/usr/bin/env bash
# Install commonly used gVisor runtimes.

for gvisor_bin in runsc runsc-dev; do
    # Install the default version (alias)
    sudo $gvisor_bin install -runtime "$gvisor_bin"
    for platform in ptrace kvm; do
        label="$gvisor_bin-$platform"
        # Install the default version
        sudo $gvisor_bin install -runtime "$label" -- --platform=$platform
        # Install the debug version
        sudo $gvisor_bin install -runtime "$label-debug" -- --platform=$platform \
        --debug-log="/tmp/$gvisor_bin/" --debug --strac
        # Install the profile version
        sudo $gvisor_bin install -runtime "$label-prof" -- --platform=$platform \
        --profile
    done
done

sudo systemctl restart docker
