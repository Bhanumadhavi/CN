# Bit Stuffing Implementation

FLAG = '01111110'

def bit_stuffing(data):
    stuffed_data = ''
    count = 0
    for bit in data:
        if bit == '1':
            count += 1
            stuffed_data += bit
            if count == 5:
                stuffed_data += '0'  # Stuff a '0' after 5 consecutive '1's
                count = 0
        else:
            stuffed_data += bit
            count = 0
    # Add frame delimiter
    stuffed_data = FLAG + stuffed_data + FLAG
    return stuffed_data

def bit_unstuffing(frame):
    # Remove starting and ending FLAG
    data = frame[len(FLAG):-len(FLAG)]
    unstuffed_data = ''
    count = 0
    for bit in data:
        if bit == '1':
            count += 1
            unstuffed_data += bit
        else:
            if count == 5:
                # Skip stuffed '0'
                count = 0
                continue
            unstuffed_data += bit
            count = 0
    return unstuffed_data

# Test the program
data = "011111101111110"
print("Original Data:", data)
stuffed = bit_stuffing(data)
print("Stuffed Data:", stuffed)
unstuffed = bit_unstuffing(stuffed)
print("Unstuffed Data:", unstuffed)
