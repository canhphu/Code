/* (C) 2021 Nguyen Ba Ngoc (bangoc) */

/** @file
 * @brief Các thành phần nền tảng: Biểu thức tính toán con trỏ,
 * đo thời gian thực thi, v.v..
 */

#ifndef BASE_CORE_H_
#define BASE_CORE_H_

#include <stddef.h>
#include <time.h>

#define CONTAINER_OF(ptr, type, member) \
  ((type *)((void*)(ptr) - offsetof(type, member)))

#define BENCH(NAME, ITER, ...)    do { \
        double _sum = 0, _start, _stop; \
        for (int _i = 0; _i < (ITER); ++_i) { \
          _start = clock(); \
          { __VA_ARGS__; } \
          _stop = clock(); \
          _sum += _stop - _start; \
        } \
        if ((ITER) > 1) { \
          printf("%s (trung bình %d lượt) = %.5g s\n", \
                (NAME), (ITER),  (_sum/CLOCKS_PER_SEC) / (ITER)); \
        } else { \
          printf("%s: %5g s\n", (NAME), _sum/CLOCKS_PER_SEC); \
        }\
    } while (0)

#define BENCH1_START() \
   long _bench1_start = clock()
#define BENCH1_END() \
   long _bench1_end = clock(); \
   printf("Time: %.3f\n", (double)(_bench1_end - _bench1_start)/CLOCKS_PER_SEC)

#endif  // BASE_CORE_H_