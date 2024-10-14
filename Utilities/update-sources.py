#!/usr/bin/env python3
#
# This script updates the ./Sources/dlmalloc/*.c files with the latest version
# from the dlmalloc sources.

import os
import shutil


def copy_wasilibc_files(package_root):
    files = [
        # [SOURCE, DESTINATION]
        ['Vendor/wasi-libc/dlmalloc/src/dlmalloc.c', 'Sources/dlmalloc/wasm/dlmalloc.c'],
        ['Vendor/wasi-libc/dlmalloc/src/malloc.c', 'Sources/dlmalloc/wasm/malloc.c'],
        ['Vendor/wasi-libc/libc-bottom-half/sources/sbrk.c', 'Sources/dlmalloc/wasm/sbrk.c'],
        ['Vendor/wasi-libc/libc-top-half/musl/src/string/memset.c', 'Sources/dlmalloc/wasm/memset.c'],
        ['Vendor/wasi-libc/libc-top-half/musl/src/string/memmove.c', 'Sources/dlmalloc/wasm/memmove.c'],
        ['Vendor/wasi-libc/libc-top-half/musl/src/string/memcpy.c', 'Sources/dlmalloc/wasm/memcpy.c'],
        ['Vendor/wasi-libc/libc-bottom-half/sources/abort.c', 'Sources/dlmalloc/wasm/abort.c'],
    ]
    for internal_bottom_header in [
        '__errno.h',
        '__errno_values.h',
        '__functions_malloc.h',
        '__macro_PAGESIZE.h',
        '__typedef_blksize_t.h',
        '__typedef_clock_t.h',
        '__typedef_clockid_t.h',
        '__typedef_nlink_t.h',
        '__typedef_off_t.h',
        '__typedef_ssize_t.h',
        '__typedef_suseconds_t.h',
        '__typedef_time_t.h',
        '__functions_malloc.h',
        '__functions_memcpy.h',
        'sys/types.h',
        'wasi/api.h',
        'stdlib.h',
    ]:
        files.append([
            os.path.join('Vendor/wasi-libc/libc-bottom-half/headers/public', internal_bottom_header),
            os.path.join('Sources/dlmalloc/wasm/internal-headers', internal_bottom_header)
        ])
    for internal_top_header in [
        'endian.h',
        'errno.h',
        'features.h',
        'malloc.h',
    ]:
        files.append([
            os.path.join('Vendor/wasi-libc/libc-top-half/musl/include', internal_top_header),
            os.path.join('Sources/dlmalloc/wasm/internal-headers', internal_top_header)
        ])

    files.append([
        'Vendor/wasi-libc/dlmalloc/include/unistd.h',
        'Sources/dlmalloc/wasm/internal-headers/unistd.h'
    ])

    for file in files:
        source = os.path.join(package_root, file[0])
        source = os.path.relpath(source)
        destination = os.path.join(package_root, file[1])
        destination = os.path.relpath(destination)

        print(f"Copying {source} to {destination}")
        os.makedirs(os.path.dirname(destination), exist_ok=True)
        shutil.copyfile(source, destination)


def apply_patches(package_root):
    # Apply patches ./Patches/*.patch
    patches_dir = os.path.join(package_root, 'Patches')
    patches = os.listdir(patches_dir)
    for patch in sorted(patches):
        if not patch.endswith('.patch'):
            continue
        patch_path = os.path.join(patches_dir, patch)
        patch_path = os.path.relpath(patch_path)
        print(f"Applying patch {patch_path}")
        os.system(f"patch -p1 < {patch_path}")


def main():
    package_root = os.path.join(os.path.dirname(__file__), '..')
    copy_wasilibc_files(package_root)
    apply_patches(package_root)


if __name__ == '__main__':
    main()
