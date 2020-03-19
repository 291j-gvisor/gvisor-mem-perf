RESULTS = malloc.pdf
RESULTS += mmap-iter-anon.pdf mmap-iter-private.pdf mmap-iter-shared.pdf
RESULTS += mmap-size-anon.pdf mmap-size-private.pdf mmap-size-shared.pdf
RESULTS += prof-iter.pdf prof-size.pdf

all: $(RESULTS)

malloc.pdf:
	./plot-malloc.py ../gcp-malloc $@

mmap-iter-anon.pdf:
	./plot-exp1.py -m mmap_anon_nofree ../exp1_anon $@

mmap-iter-private.pdf:
	./plot-exp1.py -m mmap_private_nofree ../exp1_private $@

mmap-iter-shared.pdf:
	./plot-exp1.py -m mmap_shared_nofree ../exp1_shared $@

mmap-size-anon.pdf:
	./plot-exp2.py -m mmap_anon_nofree ../exp2_anon $@

mmap-size-private.pdf:
	./plot-exp2.py -m mmap_private_nofree ../exp2_private $@

mmap-size-shared.pdf:
	./plot-exp2.py -m mmap_shared_nofree ../exp2_shared $@

prof-iter.pdf:
	./plot-time-report-exp1.py ../time_exp1_shared $@

prof-size.pdf:
	./plot-time-report-exp2.py ../time_exp2_anon $@

clean:
	rm $(RESULTS)

.PHONY: all clean
