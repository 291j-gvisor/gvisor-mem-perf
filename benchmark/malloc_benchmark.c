// Adapted from:
// https://github.com/EthanGYoung/gvisor_analysis/blob/master/experiments/execute/memory_performance/nofree/malloc_nofree.c
#include <malloc.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#include "util.h"

void notouch_nofree(int iterations, int malloc_size) {
  struct timespec start, end;
  char *str;
  clock_gettime(CLOCK_MONOTONIC, &start);
  void *p;
  for (int i = 0; i < iterations; ++i) {
    // malloc
    p = malloc(malloc_size);
    // no touch
    // no free
  }

  clock_gettime(CLOCK_MONOTONIC, &end);
  double elapsed = get_elapsed_in_s(start, end);
  printf("%.12f\n", elapsed / iterations);
  free(p);
}

void notouch_free(int iterations, int malloc_size) {
  struct timespec start, end;
  char *str;
  clock_gettime(CLOCK_MONOTONIC, &start);

  for (int i = 0; i < iterations; ++i) {
    // malloc
    void *p = malloc(malloc_size);
    // no touch
    // do free
    free(p);
  }

  clock_gettime(CLOCK_MONOTONIC, &end);
  double elapsed = get_elapsed_in_s(start, end);
  printf("%.12f\n", elapsed / iterations);
}

void touch_nofree(int iterations, int malloc_size) {
  struct timespec start, end;
  char *str;
  clock_gettime(CLOCK_MONOTONIC, &start);
  void *p;

  for (int i = 0; i < iterations; ++i) {
    // malloc
    p = malloc(malloc_size);
    // do touch
    memset(p, 0, malloc_size);
    // no free
  }

  clock_gettime(CLOCK_MONOTONIC, &end);
  double elapsed = get_elapsed_in_s(start, end);
  printf("%.12f\n", elapsed / iterations);
  free(p);
}

void touch_free(int iterations, int malloc_size) {
  struct timespec start, end;
  char *str;
  clock_gettime(CLOCK_MONOTONIC, &start);

  for (int i = 0; i < iterations; ++i) {
    // malloc
    void *p = malloc(malloc_size);
    // do touch
    memset(p, 0, malloc_size);
    // do free
    free(p);
  }

  clock_gettime(CLOCK_MONOTONIC, &end);
  double elapsed = get_elapsed_in_s(start, end);
  printf("%.12f\n", elapsed / iterations);
}

int main(int argc, char *argv[]) {
  // parse command line args
  if (argc < 4) {
    printf(
        "ERROR: Usage: ./malloc_free <iterations> <malloc size> <mode> [mmap "
        "threshold]\n");
    return 1;
  }
  if (argc > 5) {
    printf(
        "ERROR: Usage: ./malloc_free <iterations> <malloc size> <mode> [mmap "
        "threshold]\n");
    return 1;
  }
  int iterations = atoi(argv[1]);
  int malloc_size = atoi(argv[2]);
  int mode = atoi(argv[3]);
  if (argc == 5) {
    if (mallopt(M_MMAP_THRESHOLD, atoi(argv[4])) == 0) {
      perror("mallopt");
      return 1;
    }
  }

  // benchmark
  switch (mode) {
    case 0:
      notouch_nofree(iterations, malloc_size);
      break;
    case 1:
      notouch_free(iterations, malloc_size);
      break;
    case 2:
      touch_nofree(iterations, malloc_size);
      break;
    case 3:
      touch_free(iterations, malloc_size);
      break;
    default:
      printf("ERROR: Invalid mode!\n");
      return 1;
  }

  return 0;
}
