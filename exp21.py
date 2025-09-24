# Character Stuffing Implementation

FLAG = 'F'   # Frame delimiter
ESC = 'E'    # Escape character

def char_stuffing(data):
    stuffed_data = ''
    for ch in data:
        if ch == FLAG or ch == ESC:
            stuffed_data += ESC  # Add escape before special char
        stuffed_data += ch
    # Add FLAG at start and end of frame
    stuffed_data = FLAG + stuffed_data + FLAG
    return stuffed_data

def char_unstuffing(frame):
    # Remove starting and ending FLAG
    data = frame[1:-1]
    unstuffed_data = ''
    i = 0
    while i < len(data):
        if data[i] == ESC:
            i += 1  # Skip the escape character
        unstuffed_data += data[i]
        i += 1
    return unstuffed_data

# Test the program
data = "HELLOFEEWORLD"
print("Original Data:", data)
stuffed = char_stuffing(data)
print("Stuffed Data:", stuffed)
unstuffed = char_unstuffing(stuffed)
print("Unstuffed Data:", unstuffed)
