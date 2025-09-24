# Checksum Implementation

def calculate_checksum(data):
    """
    Calculate simple checksum by summing ASCII values of characters
    and taking modulo 256 (1 byte)
    """
    checksum = 0
    for char in data:
        checksum += ord(char)
    checksum %= 256
    return checksum

def sender(data):
    # Calculate checksum
    checksum = calculate_checksum(data)
    # Frame = data + checksum
    frame = data + chr(checksum)
    print("Data sent:", frame)
    return frame

def receiver(frame):
    # Extract data and checksum
    data = frame[:-1]
    received_checksum = ord(frame[-1])
    # Recalculate checksum
    calculated_checksum = calculate_checksum(data)
    print("Received Data:", data)
    print("Received Checksum:", received_checksum)
    print("Calculated Checksum:", calculated_checksum)
    # Verify data
    if received_checksum == calculated_checksum:
        print("Data is correct.")
    else:
        print("Data is corrupted!")

# Test the program
data = "HELLO123"
print("Original Data:", data)

# Sender side
frame = sender(data)

# Receiver side
receiver(frame)

# Test with corrupted data
print("\n--- Simulate Corruption ---")
corrupted_frame = frame[:-1] + chr(ord(frame[-1]) + 1)  # Modify checksum
receiver(corrupted_frame)
