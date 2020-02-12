.PHONY: fmt
fmt:
	find benchmark -name '*.c' -exec clang-format -style=file -i {} \;
