#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/mman.h>
#include <time.h>
#include <unistd.h>
#include "util.h"

const int64_t MEM_MAX = 50*1024*(int64_t)1048576;

int main(int argc, char *argv[]) {
  // parse command line args
  if (argc != 4 && argc != 3) {
    printf("ERROR: Usage: ./mmap_* <iterations> <mmap size> [warmup time]\n");
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
    warmupTime = strtod(argv[3], NULL);
  }

  void **maparr = malloc(sizeof(void*)*arrlength);
  // warmup
  struct timespec s, e;
  clock_gettime(CLOCK_MONOTONIC, &s);
  while (1 && warmupTime) {
    maparr[warmupIt++] = mmap(0, warmupSize, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    if (maparr[warmupIt-1] == -1) {
      printf("%ld\n", warmupIt-1);
      perror("mmap");
      return -1;
    }
    if (warmupIt % 1000 == 0) {
      clock_gettime(CLOCK_MONOTONIC, &e);
      if (get_elapsed_in_s(s, e) >= warmupTime || (warmupIt+1000) * warmupSize > MEM_MAX || warmupIt >= 2621440-1000) break;
      if (arrlength - warmupIt <= 2000) {
        arrlength = 2 * arrlength;
        maparr = realloc(maparr, arrlength * sizeof(void*));
        if (maparr==0) {
          perror("realloc");
          return -1;   
        }
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
//  if (e.tv_nsec != 0)printf("%ld iterations' warm up takes %lf seconds\n", warmupIt,get_elapsed_in_s(s, e));
  
  void * map;
  tsc_warmup();
//printf("///////////////////////////////////////////////////\n");
//printf("///////////////////////////////////////////////////\n");
//printf("///////////////////////////////////////////////////\n");
//printf("///////////////////////////////////////////////////\n");
//printf("///////////////////////////////////////////////////\n");
  int64_t begin = rdtsc_s();
  for (int i = 0; i < iterations; i++) {
    map = mmap(0, mapSize, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
  }
  int64_t end = rdtsc_e ();
//printf("///////////////////////////////////////////////////\n");
//printf("///////////////////////////////////////////////////\n");
//printf("///////////////////////////////////////////////////\n");
//printf("///////////////////////////////////////////////////\n");
//printf("///////////////////////////////////////////////////\n");
//  clock_gettime(CLOCK_MONOTONIC, &end);
//  double elapsed = get_elapsed_in_s(start, end);
  double elapsed = end - begin;
  printf("%.12f\n", elapsed / iterations / freq);
  return 0;
}
