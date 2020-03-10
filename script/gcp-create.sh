#!/usr/bin/env bash

# Create a GCP instance with nested virtualization enabled
# https://cloud.google.com/compute/docs/instances/enable-nested-virtualization-vm-instances
gcloud compute disks create image-disk \
    --image-project ubuntu-os-cloud \
    --image-family ubuntu-1804-lts \
    --zone us-west2-a
gcloud compute images create nested-vm-image \
    --source-disk image-disk \
    --source-disk-zone us-west2-a \
    --licenses "https://compute.googleapis.com/compute/v1/projects/vm-options/global/licenses/enable-vmx"
gcloud compute instances create gvisor-dev \
    --machine-type n1-standard-4 \
    --image nested-vm-image \
    --zone us-west2-a \

# Delete temporary constructs
gcloud compute disks delete image-disk
gcloud compute images delete nested-vm-image
