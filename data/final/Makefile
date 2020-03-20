EXT = png
RESULTS = malloc-free.$(EXT) malloc-nofree.$(EXT)
RESULTS += mmap-iter-anon.$(EXT) mmap-iter-private.$(EXT) mmap-iter-shared.$(EXT)
RESULTS += mmap-size-anon.$(EXT) mmap-size-private.$(EXT) mmap-size-shared.$(EXT)
RESULTS += prof-iter.$(EXT) prof-size.$(EXT)

all: $(RESULTS)

malloc-free.$(EXT):
	./plot-malloc.py --free ../gcp-malloc $@

malloc-nofree.$(EXT):
	./plot-malloc.py ../gcp-malloc $@

mmap-iter-anon.$(EXT):
	./plot-exp1.py ../exp1_anon $@

mmap-iter-private.$(EXT):
	./plot-exp1.py ../exp1_private $@

mmap-iter-shared.$(EXT):
	./plot-exp1.py ../exp1_shared $@

mmap-size-anon.$(EXT):
	./plot-exp2.py ../exp2_anon $@

mmap-size-private.$(EXT):
	./plot-exp2.py ../exp2_private $@

mmap-size-shared.$(EXT):
	./plot-exp2.py ../exp2_shared $@

prof-iter.$(EXT):
	./plot-time-report-exp1.py ../time_exp1_shared $@

prof-size.$(EXT):
	./plot-time-report-exp2.py ../time_exp2_anon $@

clean:
	rm $(RESULTS)

.PHONY: all clean
