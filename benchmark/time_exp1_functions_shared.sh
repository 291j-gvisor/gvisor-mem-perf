sleep 10
docker run --runtime=runsc-dev -m 50g -it --rm mmap_test /bin/bash -c "bin/mmap_shared_nofree 5000 4096; bin/mmap_shared_nofree 5000 4096; bin/mmap_shared_nofree 5000 4096; bin/mmap_shared_nofree 5000 4096; bin/mmap_shared_nofree 5000 4096; bin/mmap_shared_nofree 5000 4096; bin/mmap_shared_nofree 5000 4096" > time_exp1_shared/time_report_5000
sleep 1
docker run --runtime=runsc-dev -m 50g -it --rm mmap_test /bin/bash -c "bin/mmap_shared_nofree 10000 4096; bin/mmap_shared_nofree 10000 4096; bin/mmap_shared_nofree 10000 4096; bin/mmap_shared_nofree 10000 4096; bin/mmap_shared_nofree 10000 4096; bin/mmap_shared_nofree 10000 4096; bin/mmap_shared_nofree 10000 4096" > time_exp1_shared/time_report_10000
sleep 1
docker run --runtime=runsc-dev -m 50g -it --rm mmap_test /bin/bash -c "bin/mmap_shared_nofree 25000 4096; bin/mmap_shared_nofree 25000 4096; bin/mmap_shared_nofree 25000 4096; bin/mmap_shared_nofree 25000 4096; bin/mmap_shared_nofree 25000 4096; bin/mmap_shared_nofree 25000 4096; bin/mmap_shared_nofree 25000 4096" > time_exp1_shared/time_report_25000

