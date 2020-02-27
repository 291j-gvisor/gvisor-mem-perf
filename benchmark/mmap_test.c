#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/mman.h>
#include <time.h>
#include <unistd.h>
#include "util.h"

int main(int argc, char *argv[]) {
  unsigned long offset = 0;
  unsigned long mapSize = 1024*1024*1024;
  int *map = NULL;
  struct timespec start, end;

  printf("mmap: %x\n", map);
  while (1) {
    map = mmap(NULL, mapSize, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    munmap(map, mapSize);
  }


//  getchar();
  return 0;
}
