#ifndef SWIFT_DLMALLOC_H
#define SWIFT_DLMALLOC_H

#include <stddef.h>

void *malloc (size_t);
void *calloc (size_t, size_t);
void *realloc (void *, size_t);
void free (void *);

#endif // SWIFT_DLMALLOC_H
