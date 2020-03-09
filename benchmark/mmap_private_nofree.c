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
  if (argc != 4 && argc != 3) {
    printf("ERROR: Usage: ./mmap_* <iterations> <mmap size> [warmup iterations]\n");
    return 1;
  }

  // const size_t pageSize = sysconf(_SC_PAGESIZE);
  unsigned long iterations = strtoul(argv[1], NULL, 10);
  unsigned long mapSize = strtoul(argv[2], NULL, 10);
  unsigned long offset = 0;
  unsigned long warmupIt = 0;
  double warmupTime = 2.0;
  unsigned long warmupSize = mapSize;
  unsigned long arrlength = 500000;
  if (argc == 4) {
    warmupIt = strtoul(argv[3], NULL, 10);
  }

  void **maparr = malloc(sizeof(void*)*warmupIt);
  // warmup
  struct timespec s, e;
  clock_gettime(CLOCK_MONOTONIC, &s);
  while (1) {
    maparr[warmupIt++] = mmap(0, warmupSize, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    if (warmupIt % 1000 == 0) {
      clock_gettime(CLOCK_MONOTONIC, &e);
      if (get_elapsed_in_s(s, e) >= warmupTime) break;
      if (arrlength - warmupIt <= 2000) {
        arrlength = 2 * arrlength;
        maparr = realloc(maparr, arrlength * sizeof(void*));
      }
    }
  }
//  for (int i = 0; i < warmupIt; ++i) {
//    maparr[i] = mmap(0, warmupSize, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
//  }
  for (int i = 0; i < warmupIt; ++i) {
    munmap(maparr[i], warmupSize);  
  }
  free(maparr);
//  printf("warm up takes %lf seconds\n", get_elapsed_in_s(s, e));

  int fd = open("data", O_RDWR | O_CREAT | O_TRUNC, 0600); 
  printf("%ld\n", mapSize);
  lseek(fd, mapSize, SEEK_SET);

  void * map;
  tsc_warmup();

//printf("///////////////////////////////////////////////////\n");
//printf("///////////////////////////////////////////////////\n");
//printf("///////////////////////////////////////////////////\n");
//printf("///////////////////////////////////////////////////\n");
//printf("///////////////////////////////////////////////////\n");
  int64_t begin = rdtsc_s();
  for (int i = 0; i < iterations; i++) {
    map = mmap(NULL, mapSize, PROT_READ | PROT_WRITE, MAP_PRIVATE, fd, 0);
  }
  int64_t end = rdtsc_e ();
//printf("///////////////////////////////////////////////////\n");
//printf("///////////////////////////////////////////////////\n");
//printf("///////////////////////////////////////////////////\n");
//printf("///////////////////////////////////////////////////\n");
//printf("///////////////////////////////////////////////////\n");

  double elapsed = end - begin;
  printf("%.12f\n", elapsed / iterations / freq);
  return 0;
}
