BINDIR = bin
BINS = $(patsubst ./%.c,$(BINDIR)/%,$(shell find . -type f -name "*.c"))

.PHONY: all
all: $(BINS)

$(BINS): bin/%: %.c util.h | $(BINDIR)
	gcc -std=gnu99 -o $@ $<

$(BINDIR):
	mkdir $@

.PHONY: clean
clean:
	rm -rf $(BINDIR)
