#!/usr/bin/env bash
rm -rf rootfs
mkdir rootfs
docker export $(docker create mmap_test) | tar -xf - -C rootfs

