#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/mman.h>
#include <time.h>
#include <unistd.h>
#include "util.h"

#define WARMUP 100000

int main(int argc, char *argv[]) {
  // parse command line args
  if (argc != 4 && argc != 3) {
    printf("ERROR: Usage: ./mmap_* <iterations> <mmap size> [warmup iterations]\n");
    return 1;
  }

  // const size_t pageSize = sysconf(_SC_PAGESIZE);
  unsigned long iterations = strtoul(argv[1], NULL, 10);
  unsigned long mapSize = strtoul(argv[2], NULL, 10);
  unsigned long offset = 0;
  unsigned long warmup = 0;
  if (argc == 4) {
    warmup = strtoul(argv[3], NULL, 10);
  }

  int *map;
  // warmup
  struct timespec start, end;
//  clock_gettime(CLOCK_MONOTONIC, &start);
  for (int i = 0; i < WARMUP; i++) {
    map = mmap(0, mapSize, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
  }
//  clock_gettime(CLOCK_MONOTONIC, &end);
//  printf("warm up takes %lf seconds\n", get_elapsed_in_s(start, end));

  clock_gettime(CLOCK_MONOTONIC, &start);
//printf("///////////////////////////////////////////////////\n");
//printf("///////////////////////////////////////////////////\n");
//printf("///////////////////////////////////////////////////\n");
//printf("///////////////////////////////////////////////////\n");
//printf("///////////////////////////////////////////////////\n");
  for (int i = 0; i < iterations; i++) {
    map = mmap(0, mapSize, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
  }
//printf("///////////////////////////////////////////////////\n");
//printf("///////////////////////////////////////////////////\n");
//printf("///////////////////////////////////////////////////\n");
//printf("///////////////////////////////////////////////////\n");
//printf("///////////////////////////////////////////////////\n");
  clock_gettime(CLOCK_MONOTONIC, &end);
  double elapsed = get_elapsed_in_s(start, end);
  printf("%.12f\n", elapsed / iterations);
  return 0;
}
