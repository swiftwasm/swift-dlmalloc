// swift-tools-version: 5.10

import PackageDescription

let package = Package(
    name: "dlmalloc",
    products: [
        .library(
            name: "dlmalloc",
            targets: ["dlmalloc"]),
    ],
    targets: [
        .target(
            name: "dlmalloc",
            exclude: ["wasm/"],
            cSettings: [
                .headerSearchPath("wasm/internal-headers"),
                // NOTE: Keep the value in sync with https://github.com/WebAssembly/wasi-libc/blob/wasi-sdk-27/Makefile#L44
                .define("BULK_MEMORY_THRESHOLD", to: "32"),
            ]
        ),
    ]
)
