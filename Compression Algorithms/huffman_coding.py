import heapq
from collections import defaultdict

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    frequency = defaultdict(int)
    for char in text:
        frequency[char] += 1

    priority_queue = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left_node = heapq.heappop(priority_queue)
        right_node = heapq.heappop(priority_queue)
        merged_node = HuffmanNode(None, left_node.freq + right_node.freq)
        merged_node.left = left_node
        merged_node.right = right_node
        heapq.heappush(priority_queue, merged_node)

    return priority_queue[0]

def build_huffman_codes(node, prefix='', codes={}):
    if node:
        if node.char:
            codes[node.char] = prefix
        build_huffman_codes(node.left, prefix + '0', codes)
        build_huffman_codes(node.right, prefix + '1', codes)
    return codes

def huffman_compress(text):
    root = build_huffman_tree(text)
    codes = build_huffman_codes(root)
    encoded_text = ''.join(codes[char] for char in text)
    return encoded_text, codes

def huffman_decompress(encoded_text, codes):
    decoded_text = ''
    current_code = ''
    for bit in encoded_text:
        current_code += bit
        for char, code in codes.items():
            if code == current_code:
                decoded_text += char
                current_code = ''
                break
    return decoded_text

# Example Usage
original_text = "Huffman coding is a compression algorithm"
encoded_text, codes = huffman_compress(original_text)
print("Encoded:", encoded_text)
decoded_text = huffman_decompress(encoded_text, codes)
print("Decoded:", decoded_text)
