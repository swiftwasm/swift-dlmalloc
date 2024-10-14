# Example of swift-dlmalloc usage

This is a simple example of how to use the `swift-dlmalloc` package.

## Build and run

```console
$ swift build -c release --triple wasm32-unknown-none-wasm -debug-info-format=none
$ wasmtime run .build/release/Examples.wasm
Hello, world!
malloc(8) = 0x106d0
*(0x106d0) = 42
```
