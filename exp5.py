
def xor(a, b):
    """Perform XOR operation between two binary strings"""
    result = []
    for i in range(1, len(b)):
        result.append('0' if a[i] == b[i] else '1')
    return ''.join(result)

def crc_remainder(input_data, polynomial):
    """Calculate CRC remainder"""
    padded_data = input_data + '0'*(len(polynomial)-1)
    remainder = padded_data[:len(polynomial)]
    
    for i in range(len(polynomial), len(padded_data)+1):
        if remainder[0] == '1':
            remainder = xor(remainder, polynomial) + (padded_data[i] if i < len(padded_data) else '')
        else:
            remainder = xor('0'*len(polynomial), remainder) + (padded_data[i] if i < len(padded_data) else '')
    return remainder

def string_to_binary(data):
    """Convert string to binary representation"""
    return ''.join(format(ord(c), '08b') for c in data)

data = input("Enter a string of characters: ")
binary_data = string_to_binary(data)
print("Binary representation of data:", binary_data)

crc_polynomials = {
    "CRC-12": "1100000001111",    
    "CRC-16": "11000000000000101", 
    "CRC-CCITT": "10001000000100001" 
}

# Calculate CRCs
for name, poly in crc_polynomials.items():
    remainder = crc_remainder(binary_data, poly)
    print(f"{name} remainder (CRC): {remainder}")
