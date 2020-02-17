// Adapted from:
// https://github.com/EthanGYoung/gvisor_analysis/blob/master/experiments/execute/memory_performance/free/malloc_free.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#include "util.h"

int main(int argc, char *argv[]) {
  // parse command line args
  if (argc != 3) {
    printf("ERROR: Usage: ./malloc_free <iterations> <malloc size>\n");
    return 1;
  }
  int iterations = atoi(argv[1]);
  int malloc_size = atoi(argv[2]);

  // benchmark
  struct timespec start, end;
  char *str;
  clock_gettime(CLOCK_MONOTONIC, &start);

  for (int i = 0; i < iterations; ++i) {
    // malloc
    str = (char *)malloc(malloc_size);
    strcpy(str, "test");
    if (strcmp(str, "test") != 0) {
      printf("ERROR: Failed to read from str\n");
      return 0;
    }

    // free
    free(str);
  }

  clock_gettime(CLOCK_MONOTONIC, &end);
  double elapsed = get_elapsed_in_s(start, end);
  printf("%.12f\n", elapsed / iterations);

  return 0;
}
