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

static __inline__ void tsc_warmup(void)
{
  unsigned a, d; 
  asm volatile("cpuid" ::: "%rax", "%rbx", "%rcx", "%rdx");
  asm volatile("rdtsc" : "=a" (a), "=d" (d)); 
  asm volatile("rdtscp" : "=a" (a), "=d" (d)); 
  asm volatile("cpuid" ::: "%rax", "%rbx", "%rcx", "%rdx");
  asm volatile("cpuid" ::: "%rax", "%rbx", "%rcx", "%rdx");
  asm volatile("rdtsc" : "=a" (a), "=d" (d)); 
  asm volatile("rdtscp" : "=a" (a), "=d" (d)); 
  asm volatile("cpuid" ::: "%rax", "%rbx", "%rcx", "%rdx");
  asm volatile("cpuid" ::: "%rax", "%rbx", "%rcx", "%rdx");
  asm volatile("rdtsc" : "=a" (a), "=d" (d)); 
  asm volatile("rdtscp" : "=a" (a), "=d" (d)); 
  asm volatile("cpuid" ::: "%rax", "%rbx", "%rcx", "%rdx");
}

static __inline__ int64_t rdtsc_s(void)
{
  unsigned a, d; 
  asm volatile("cpuid" ::: "%rax", "%rbx", "%rcx", "%rdx");
  asm volatile("rdtsc" : "=a" (a), "=d" (d)); 
  return ((unsigned long)a) | (((unsigned long)d) << 32); 
}

static __inline__ int64_t rdtsc_e(void)
{
  unsigned a, d; 
  asm volatile("rdtscp" : "=a" (a), "=d" (d)); 
  asm volatile("cpuid" ::: "%rax", "%rbx", "%rcx", "%rdx");
  return ((unsigned long)a) | (((unsigned long)d) << 32); 
}

const double freq=2999996000;
const double rdtscp_overhead=60; // for runsc-kvm


#endif  // UTIL_H_
