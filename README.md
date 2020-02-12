# A course project on gVisor (WIP)

## Development Environment

gVisor only works on Linux. To enable local development on different platforms including macOS and Windows, [Vagrant](https://www.vagrantup.com/) is used to set up a unified environment. The [installation](https://www.vagrantup.com/docs/installation/) is pretty straightforward, except for a known [issue](https://github.com/oracle/vagrant-boxes/issues/178#issue-536720633) with Vagrant 2.2.6 and VirtualBox 6.1 (as of Feb 2020).

Once Vagrant is installed, setting up the development environment is one command away:
```console
$ vagrant up
```

Installing gVisor from source can take a fair amount of time. Be a little bit patient. Once this step finishes, you could `ssh` into the created VM:
```console
$ vagrant ssh
```

And play with gVisor:
```console
$ docker run --runtime=runsc -it ubuntu dmesg
```

This project directory is synced with `~/work` in the VM.

To get out from the VM, just type:
```console
$ exit
```

More Vagrant commands could be found in its [documentation](https://www.vagrantup.com/docs/cli/).
