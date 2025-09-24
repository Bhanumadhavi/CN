
def leaky_bucket(bucket_capacity, leak_rate, incoming_packets):
    
    bucket = 0  
    time_unit = 0

    for packets in incoming_packets:
        time_unit += 1
        print(f"\nTime unit {time_unit}:")
        print(f"Incoming packets: {packets}")
        
        bucket += packets

        if bucket > bucket_capacity:
            overflow = bucket - bucket_capacity
            print(f"Bucket overflow! {overflow} packet(s) discarded.")
            bucket = bucket_capacity
        else:
            overflow = 0

        transmitted = min(bucket, leak_rate)
        bucket -= transmitted

        print(f"Transmitted packets: {transmitted}")
        print(f"Packets remaining in bucket: {bucket}")

    print("\nSimulation finished.")

bucket_capacity = int(input("Enter bucket capacity: "))
leak_rate = int(input("Enter leak rate (packets per unit time): "))
incoming_packets = list(map(int, input("Enter incoming packets per time unit (space separated): ").split()))

leaky_bucket(bucket_capacity, leak_rate, incoming_packets)
