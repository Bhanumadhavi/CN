import random
import time

def send_frame(frame_number):
    print(f"Sending Frame {frame_number}")

def receive_frame(frame_number):
    if random.random() < 0.1:
        print(f"Frame {frame_number} lost/corrupted!")
        return False
    print(f"Frame {frame_number} received correctly.")
    return True

def stop_and_wait(total_frames):
    frame_number = 0
    while frame_number < total_frames:
        send_frame(frame_number)
        time.sleep(0.1)  

        ack = receive_frame(frame_number)
        if ack:
            print(f"ACK received for Frame {frame_number}")
            frame_number += 1  
        else:
            print(f"Retransmitting Frame {frame_number}...\n")

total_frames = int(input("Enter total number of frames to send: "))
stop_and_wait(total_frames)
