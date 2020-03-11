sleep 10
docker run --runtime=runsc-dev -m 50g -it --rm mmap_test /bin/bash -c "bin/mmap_anon_nofree 50000 1024; bin/mmap_anon_nofree 50000 1024; bin/mmap_anon_nofree 50000 1024; bin/mmap_anon_nofree 50000 1024; bin/mmap_anon_nofree 50000 1024; bin/mmap_anon_nofree 50000 1024; bin/mmap_anon_nofree 50000 1024" > time_report_1k
sleep 1
docker run --runtime=runsc-dev -m 50g -it --rm mmap_test /bin/bash -c "bin/mmap_anon_nofree 50000 2048; bin/mmap_anon_nofree 50000 2048; bin/mmap_anon_nofree 50000 2048; bin/mmap_anon_nofree 50000 2048; bin/mmap_anon_nofree 50000 2048; bin/mmap_anon_nofree 50000 2048; bin/mmap_anon_nofree 50000 2048" > time_report_2k
sleep 1
docker run --runtime=runsc-dev -m 50g -it --rm mmap_test /bin/bash -c "bin/mmap_anon_nofree 50000 4096; bin/mmap_anon_nofree 50000 4096; bin/mmap_anon_nofree 50000 4096; bin/mmap_anon_nofree 50000 4096; bin/mmap_anon_nofree 50000 4096; bin/mmap_anon_nofree 50000 4096; bin/mmap_anon_nofree 50000 4096" > time_report_4k
sleep 1
docker run --runtime=runsc-dev -m 50g -it --rm mmap_test /bin/bash -c "bin/mmap_anon_nofree 50000 8192; bin/mmap_anon_nofree 50000 8192; bin/mmap_anon_nofree 50000 8192; bin/mmap_anon_nofree 50000 8192; bin/mmap_anon_nofree 50000 8192; bin/mmap_anon_nofree 50000 8192; bin/mmap_anon_nofree 50000 8192" > time_report_8k
sleep 1
docker run --runtime=runsc-dev -m 50g -it --rm mmap_test /bin/bash -c "bin/mmap_anon_nofree 50000 16384; bin/mmap_anon_nofree 50000 16384; bin/mmap_anon_nofree 50000 16384; bin/mmap_anon_nofree 50000 16384; bin/mmap_anon_nofree 50000 16384; bin/mmap_anon_nofree 50000 16384; bin/mmap_anon_nofree 50000 16384" > time_report_16k
sleep 1
docker run --runtime=runsc-dev -m 50g -it --rm mmap_test /bin/bash -c "bin/mmap_anon_nofree 50000 32768; bin/mmap_anon_nofree 50000 32768; bin/mmap_anon_nofree 50000 32768; bin/mmap_anon_nofree 50000 32768; bin/mmap_anon_nofree 50000 32768; bin/mmap_anon_nofree 50000 32768; bin/mmap_anon_nofree 50000 32768" > time_report_32k
sleep 1
docker run --runtime=runsc-dev -m 50g -it --rm mmap_test /bin/bash -c "bin/mmap_anon_nofree 50000 65536; bin/mmap_anon_nofree 50000 65536; bin/mmap_anon_nofree 50000 65536; bin/mmap_anon_nofree 50000 65536; bin/mmap_anon_nofree 50000 65536; bin/mmap_anon_nofree 50000 65536; bin/mmap_anon_nofree 50000 65536" > time_report_64k
sleep 1
docker run --runtime=runsc-dev -m 50g -it --rm mmap_test /bin/bash -c "bin/mmap_anon_nofree 50000 131072; bin/mmap_anon_nofree 50000 131072; bin/mmap_anon_nofree 50000 131072; bin/mmap_anon_nofree 50000 131072; bin/mmap_anon_nofree 50000 131072; bin/mmap_anon_nofree 50000 131072; bin/mmap_anon_nofree 50000 131072" > time_report_128k
sleep 1
docker run --runtime=runsc-dev -m 50g -it --rm mmap_test /bin/bash -c "bin/mmap_anon_nofree 50000 262144; bin/mmap_anon_nofree 50000 262144; bin/mmap_anon_nofree 50000 262144; bin/mmap_anon_nofree 50000 262144; bin/mmap_anon_nofree 50000 262144; bin/mmap_anon_nofree 50000 262144; bin/mmap_anon_nofree 50000 262144" > time_report_256k
sleep 1
docker run --runtime=runsc-dev -m 50g -it --rm mmap_test /bin/bash -c "bin/mmap_anon_nofree 50000 524288; bin/mmap_anon_nofree 50000 524288; bin/mmap_anon_nofree 50000 524288; bin/mmap_anon_nofree 50000 524288; bin/mmap_anon_nofree 50000 524288; bin/mmap_anon_nofree 50000 524288; bin/mmap_anon_nofree 50000 524288" > time_report_512k
sleep 1
docker run --runtime=runsc-dev -m 50g -it --rm mmap_test /bin/bash -c "bin/mmap_anon_nofree 50000 1048576; bin/mmap_anon_nofree 50000 1048576; bin/mmap_anon_nofree 50000 1048576; bin/mmap_anon_nofree 50000 1048576; bin/mmap_anon_nofree 50000 1048576; bin/mmap_anon_nofree 50000 1048576; bin/mmap_anon_nofree 50000 1048576" > time_report_1024k
