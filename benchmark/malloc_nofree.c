// Adapted from:
// https://github.com/EthanGYoung/gvisor_analysis/blob/master/experiments/execute/memory_performance/nofree/malloc_nofree.c
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <sys/time.h>
#include <sys/types.h>
#include <time.h>
#include <unistd.h>

#include "util.h"

int NUM_TRIALS;
int MALLOC_SIZE;

float execute() {
  char *str;

  // Start timer
  struct timespec ts0;
  clock_gettime(CLOCK_REALTIME, &ts0);

  for (int i = 0; i < NUM_TRIALS; i++) {
    // malloc
    str = (char *)malloc(MALLOC_SIZE);
    strcpy(str, "test");
    if (strcmp(str, "test") != 0) {
      printf("ERROR: Failed to read from str\n");
      return 0;
    }
  }

  // End timer
  struct timespec ts1;
  clock_gettime(CLOCK_REALTIME, &ts1);
  struct timespec t = diff(ts0, ts1);
  // close(fd);
  float elapsed_time = t.tv_sec + t.tv_nsec / (float)1000000000;

  return elapsed_time;
}

int main(int argc, char *argv[]) {
  // Parse command line args
  if (argc != 3) {
    printf("ERROR: Usage: ./mallocfree <number of trials> <malloc size>\n");
    return 0;
  }

  NUM_TRIALS = atoi(argv[1]);

  float total = 0;

  total = execute();

  printf(
      "LOG_OUTPUT: Average for %d trials: Open/close time average = %.12f "
      "seconds\n",
      NUM_TRIALS, total / NUM_TRIALS);

  return 0;
}
