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
  int fd = open("data", O_RDWR | O_CREAT | O_TRUNC, 0600); //6 = read+write for me!
  int size = sizeof(int) * 10;
  lseek(fd, size, SEEK_SET);


  printf("mmap: %p\n", map);
//  for (int i = 0;i < 100;++i) {
//     map = mmap(NULL, SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, -1, 0);
     map = mmap(NULL, size, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
//     munmap(map, mapSize);
//  }
    printf("mmap: %p\n", map);
//  getchar();
  munmap(map, size);
  close(fd);
  return 0;
}
