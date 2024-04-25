def lzw_compress(data):
    dictionary = {chr(i): i for i in range(256)}
    result = []
    w = ""
    for c in data:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            dictionary[wc] = len(dictionary)
            w = c
    if w:
        result.append(dictionary[w])
    return result

def lzw_decompress(compressed_data):
    dictionary = {i: chr(i) for i in range(256)}
    result = ""
    w = chr(compressed_data.pop(0))
    result += w
    for k in compressed_data:
        entry = ""
        if k in dictionary:
            entry = dictionary[k]
        elif k == len(dictionary):
            entry = w + w[0]
        result += entry
        dictionary[len(dictionary)] = w + entry[0]
        w = entry
    return result

# Example Usage:
data = "ABABABAABABABBBBBB"
compressed_data = lzw_compress(data)
print("Compressed:", compressed_data)
decompressed_data = lzw_decompress(compressed_data)
print("Decompressed:", decompressed_data)
