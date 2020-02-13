#ifndef UTIL_H_
#define UTIL_H_

#include <time.h>

static inline struct timespec get_elapsed(struct timespec start, struct timespec end) {
  struct timespec elapsed;
  if ((end.tv_nsec - start.tv_nsec) < 0) {
    elapsed.tv_sec = end.tv_sec - start.tv_sec - 1;
    elapsed.tv_nsec = end.tv_nsec - start.tv_nsec + 1000000000;
  } else {
    elapsed.tv_sec = end.tv_sec - start.tv_sec;
    elapsed.tv_nsec = end.tv_nsec - start.tv_nsec;
  }
  return elapsed;
}

static inline double get_elapsed_in_s(struct timespec start, struct timespec end) {
  struct timespec elapsed = get_elapsed(start, end);
  return elapsed.tv_sec + elapsed.tv_nsec * 1e-9;
}

#endif  // UTIL_H_
