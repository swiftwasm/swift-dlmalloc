import dlmalloc

@_extern(wasm, module: "wasi_snapshot_preview1", name: "fd_write")
@_extern(c)
func fd_write(fd: Int32, iovs: UnsafeRawPointer, iovs_len: Int32, nwritten: UnsafeMutablePointer<Int32>) -> Int32

func _print(_ string: String) {
    var string = string
    string.withUTF8 { string in
        withUnsafeTemporaryAllocation(byteCount: 8, alignment: 4) { iov in
            let iov = iov.baseAddress!
            iov.advanced(by: 0).storeBytes(of: string.baseAddress!, as: UnsafeRawPointer.self)
            iov.advanced(by: 4).storeBytes(of: Int32(string.count), as: Int32.self)
            var nwritten: Int32 = 0
            _ = fd_write(fd: 1, iovs: iov, iovs_len: 1, nwritten: &nwritten)
        }
    }
}

func hex(_ ptr: UnsafeRawPointer) -> String {
    return "0x\(String(UInt(bitPattern: ptr), radix: 16))"
}

@_expose(wasm)
@_cdecl("_start")
public func main() {
    _print("Hello, world!\n")

    let ptr = dlmalloc.malloc(8)!
    ptr.storeBytes(of: 42, as: Int.self)
    _print("malloc(8) = \(hex(ptr))\n")
    _print("*(\(hex(ptr))) = \(ptr.load(as: Int.self))\n")

    dlmalloc.free(ptr)
}
