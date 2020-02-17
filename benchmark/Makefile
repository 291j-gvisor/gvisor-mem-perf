BINDIR = bin
BINS = $(patsubst ./%.c,$(BINDIR)/%,$(shell find . -name '*.c'))

.PHONY: all
all: $(BINS)

$(BINS): $(BINDIR)/%: %.c util.h | $(BINDIR)
	gcc -std=gnu99 -o $@ $<

$(BINDIR):
	mkdir $@

.PHONY: clean
clean:
	rm -rf $(BINDIR)

.PHONY: fmt
fmt:
	find . -name '*.c' -exec clang-format -style=file -i {} \;
