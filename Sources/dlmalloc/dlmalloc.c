#if __wasm__
#  define LACKS_STRING_H
#  include <stddef.h>
void *memcpy (void *__restrict, const void *__restrict, size_t);
void *memset (void *, int, size_t);
void abort(void);
_Thread_local int errno = 0;
#  include "./wasm/dlmalloc.c"
#  include "./wasm/sbrk.c"
#  include "./wasm/memcpy.c"
#  include "./wasm/memset.c"
#  include "./wasm/memmove.c"
#  include "./wasm/abort.c"
#else
#  error "Unsupported target platform. Contribution for porting to the platform is more than welcome!"
#endif
