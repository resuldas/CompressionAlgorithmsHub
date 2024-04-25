import lzma

def lzma_compress(data):
    return lzma.compress(data.encode())

def lzma_decompress(compressed_data):
    return lzma.decompress(compressed_data).decode()

# Example Usage:
data = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
compressed_data = lzma_compress(data)
print("Compressed data:", compressed_data)
decompressed_data = lzma_decompress(compressed_data)
print("Decompressed data:", decompressed_data)
