def delta_encode(data):
    encoded = [data[0]]
    for i in range(1, len(data)):
        encoded.append(data[i] - data[i - 1])
    return encoded

def delta_decode(encoded):
    decoded = [encoded[0]]
    for i in range(1, len(encoded)):
        decoded.append(decoded[i - 1] + encoded[i])
    return decoded

# Example Usage:
data = [10, 15, 20, 28, 35]
encoded_data = delta_encode(data)
print("Encoded:", encoded_data)
decoded_data = delta_decode(encoded_data)
print("Decoded:", decoded_data)

