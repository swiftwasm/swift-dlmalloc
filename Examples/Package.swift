// swift-tools-version: 6.0

import PackageDescription

let package = Package(
    name: "Examples",
    dependencies: [
        .package(path: "../"),
    ],
    targets: [
        .executableTarget(
            name: "Examples",
            dependencies: [
                .product(name: "dlmalloc", package: "swift-dlmalloc"),
            ],
            cSettings: [
                .unsafeFlags(["-fdeclspec"])
            ],
            swiftSettings: [
                .enableExperimentalFeature("Embedded"),
                .enableExperimentalFeature("Extern"),
                .unsafeFlags([
                    "-wmo", "-disable-cmo",
                    "-Xfrontend", "-gnone",
                    "-Xfrontend", "-disable-stack-protector",
                ]),
            ],
            linkerSettings: [
                .unsafeFlags([
                    "-Xclang-linker", "-nostdlib",
                    "-Xlinker", "--no-entry"
                ])
            ]
        ),
    ]
)
