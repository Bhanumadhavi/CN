
def calculate_parity_bits(data_bits):
    
    n = len(data_bits)
    r = 0
    while (2**r) < (n + r + 1):
        r += 1

    hamming_code = ['0'] * (n + r)
    j = 0  
    for i in range(1, n + r + 1):
        if (i & (i - 1)) != 0:
            hamming_code[i-1] = data_bits[j]
            j += 1

    for i in range(r):
        parity_pos = 2**i
        parity = 0
        for j in range(1, n + r + 1):
            if j & parity_pos and j != parity_pos:
                parity ^= int(hamming_code[j-1])
        hamming_code[parity_pos-1] = str(parity)

    return ''.join(hamming_code)


def detect_and_correct(hamming_code):
    """
    Detect and correct a single-bit error in the hamming code
    """
    n = len(hamming_code)
    r = 0
    while (2**r) < n + 1:
        r += 1

    error_pos = 0
    for i in range(r):
        parity_pos = 2**i
        parity = 0
        for j in range(1, n + 1):
            if j & parity_pos:
                parity ^= int(hamming_code[j-1])
        if parity != 0:
            error_pos += parity_pos

    if error_pos != 0:
        print("Error detected at position:", error_pos)
        corrected = list(hamming_code)
        corrected[error_pos-1] = '1' if corrected[error_pos-1] == '0' else '0'
        hamming_code = ''.join(corrected)
        print("Error corrected.")
    else:
        print("No error detected.")
    
    return hamming_code


data_bits = input("Enter data bits (e.g., 1011): ")
hamming_code = calculate_parity_bits(data_bits)
print("Generated Hamming Code:", hamming_code)

error_code = list(hamming_code)
pos = int(input("Enter position to simulate error (0 for no error): "))
if pos != 0:
    error_code[pos-1] = '1' if error_code[pos-1] == '0' else '0'
error_code = ''.join(error_code)

print("Received Code:", error_code)


corrected_code = detect_and_correct(error_code)
print("Corrected Hamming Code:", corrected_code)
