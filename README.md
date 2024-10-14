# swift-dlmalloc

This is a SwiftPM package for [dlmalloc](https://gee.cs.oswego.edu/dl/html/malloc.html) which is a general-purpose memory allocator written by Doug Lea.
Typically, this package is helpful when you need a memory allocator implementation for Embedded Swift applications.

## Supported Platforms

| Target triplet | Supported |
|----------------|:---------:|
| wasm32-unknown-none-wasm | ✅ |

Feel free to create a PR to add support for other platforms.

## Usage

Add the following dependency to your `Package.swift` file:

```swift
dependencies: [
    .package(url: "https://github.com/swiftwasm/swift-dlmalloc", from: "0.1.0"),
]
```

Then, add `dlmalloc` as a dependency for your target:

```swift
.executableTarget(
    name: "Examples",
    dependencies: [
        .product(name: "dlmalloc", package: "swift-dlmalloc"),
    ]
)
```

Finally, import `dlmalloc` module in your Swift code:

```swift

import dlmalloc

public func main() {
    let ptr = dlmalloc.malloc(8)!
    ptr.storeBytes(of: 42, as: Int.self)
    print("malloc(8) = \(ptr)\n")
    print("*(\(ptr)) = \(ptr.load(as: Int.self))\n")

    dlmalloc.free(ptr)
}
```

See [Examples](Examples) directory for more working examples.

## License

This package is licensed under the MIT license. See [LICENSE](LICENSE) for more info.

Portions of this software are based on the work of Doug Lea and others. See [NOTICE](NOTICE) for more info.

