import time
import queue
import threading

# Instantiate the shared data highway
data_queue = queue.Queue()

# 1. The Producer: Generates raw payloads
def raw_data_producer():
    for i in range(1, 6):
        print(f"Producer: Fetching raw record {i}...")
        time.sleep(0.2) # Simulates network latency
        data_queue.put(f"RAW_RECORD_{i}")

# 2. The Consumer: Processes payloads from the queue
def data_consumer(worker_id: int):
    while True:
        # This will block and wait if the queue is temporarily empty!
        raw_item = data_queue.get()
        
        # A standard trick: pass None into the queue to tell workers to shut down cleanly
        if raw_item is None:
            data_queue.task_done()
            print("No new item produced.")
            break
            
        print(f"Consumer Thread-{worker_id}: Processing {raw_item} into database.")
        time.sleep(0.4) # Simulates write latency
        data_queue.task_done()

if __name__ == "__main__": # This is where the script orchestrates the producer and consumers
    # Start the Producer Thread
    producer_thread = threading.Thread(target=raw_data_producer)
    producer_thread.start()
    
    # Start 2 Parallel Consumer Threads to share the processing load
    consumer_threads = []
    for uid in range(2):
        t = threading.Thread(target=data_consumer, args=(uid,))
        t.start()
        consumer_threads.append(t)
        
    # Wait for the producer to finish fetching data
    producer_thread.join()
    
    # Block the main script until all items in the queue have been fully processed
    data_queue.join()
    
    # Stop the consumers by feeding them sentinel values (None)
    for _ in range(2): # The underscore symbol "_" is a conventional "throwaway" name for a loop variable you don't need
        data_queue.put(None)
        
    for t in consumer_threads:
        t.join()
        
    print("✅ Entire pipeline finished successfully!")