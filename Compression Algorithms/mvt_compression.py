def move_to_front_encode(data):
    alphabet = list(range(256))
    encoded_data = []
    for symbol in data:
        index = alphabet.index(symbol)
        encoded_data.append(index)
        alphabet.pop(index)
        alphabet.insert(0, symbol)
    return encoded_data

def move_to_front_decode(encoded_data):
    alphabet = list(range(256))
    decoded_data = []
    for index in encoded_data:
        symbol = alphabet[index]
        decoded_data.append(symbol)
        alphabet.pop(index)
        alphabet.insert(0, symbol)
    return decoded_data

# Example Usage:
data = [65, 66, 67, 65, 68, 65, 66, 67, 65, 68]  
encoded_data = move_to_front_encode(data)
print("Encoded Data:", encoded_data)
decoded_data = move_to_front_decode(encoded_data)
print("Decoded Data:", decoded_data)