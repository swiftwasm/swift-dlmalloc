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
                .headerSearchPath("wasm/internal-headers")
            ]
        ),
    ]
)
