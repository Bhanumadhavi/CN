import random
import time

def send_frame(frame_number):
    print(f"Sending Frame {frame_number}")

def receive_frame(frame_number):
    # Simulate a 10% chance of frame loss/corruption
    if random.random() < 0.1:
        print(f"Frame {frame_number} lost/corrupted!")
        return False
    print(f"Frame {frame_number} received correctly.")
    return True

def selective_repeat(total_frames, window_size):
    next_frame = 0
    acked_frames = [False] * total_frames

    while not all(acked_frames):
        # Send frames within window
        print(f"\nSending frames {next_frame} to {min(next_frame+window_size-1, total_frames-1)}")
        sent_frames = []
        for i in range(next_frame, min(next_frame+window_size, total_frames)):
            if not acked_frames[i]:  # Only send if not yet acknowledged
                send_frame(i)
                sent_frames.append(i)
                time.sleep(0.1)  # simulate transmission delay

        # Receive acknowledgments
        for frame in sent_frames:
            ack = receive_frame(frame)
            if ack:
                acked_frames[frame] = True
            else:
                print(f"Frame {frame} will be retransmitted.")

        # Slide window: move next_frame to the first unacknowledged frame
        while next_frame < total_frames and acked_frames[next_frame]:
            next_frame += 1

# ------------------- Main Program -------------------
total_frames = int(input("Enter total number of frames to send: "))
window_size = int(input("Enter window size: "))

selective_repeat(total_frames, window_size)
