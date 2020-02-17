#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/mman.h>
#include <time.h>
#include <unistd.h>
#include "util.h"

int main(int argc, char *argv[]) {
  // parse command line args
  if (argc != 3) {
    printf("ERROR: Usage: ./malloc_free <iterations> <malloc size>\n");
    return 1;
  }

  // const size_t pageSize = sysconf(_SC_PAGESIZE);

  unsigned long iterations = strtoul(argv[1], NULL, 10);
  unsigned long mapSize = strtoul(argv[2], NULL, 10);
  unsigned long offset = 0;

  int *map;
  struct timespec start, end;
  clock_gettime(CLOCK_MONOTONIC, &start);
  int file = open("mapfile", O_RDWR);

  for (int i = 0; i < iterations; i++) {
    map = mmap(0, mapSize, PROT_READ, MAP_PRIVATE, file, offset);
    offset = offset + mapSize;
    munmap(map, mapSize);
  }

  clock_gettime(CLOCK_MONOTONIC, &end);
  double elapsed = get_elapsed_in_s(start, end);
  printf("%.12f\n", elapsed / iterations);
  close(file);
}
