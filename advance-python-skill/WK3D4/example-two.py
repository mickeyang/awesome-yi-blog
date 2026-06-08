# This example is derived from the example-one.py by the Gemini AI
# This example introduces two constant variables NUM_PRODUCERS and NUM_CONSUMERS so that
# we can use them to balance number of producers and consumers 
# by analysing the data_queue.qsize() value

import time
import queue
import threading

# --- Configuration ---
# Let's say consuming is the slow part, so we'll use more consumers.
NUM_PRODUCERS = 1
NUM_CONSUMERS = 4 # We increased this from 2 to 4
TOTAL_RECORDS_TO_PRODUCE = 20

# Instantiate the shared data highway
data_queue = queue.Queue()

# 1. The Producer: Now takes a range of work to do
def raw_data_producer(start_id, end_id):
    for i in range(start_id, end_id + 1):
        print(f"Producer: Fetching raw record {i}...")
        time.sleep(0.1) # Producer is fast
        data_queue.put(f"RAW_RECORD_{i}")

# 2. The Consumer: Processes payloads from the queue (no changes needed here)
def data_consumer(worker_id: int):
    while True:
        raw_item = data_queue.get()
        
        if raw_item is None:
            data_queue.task_done()
            break # Exit loop and shut down thread
            
        print(f"Consumer Thread-{worker_id}: Processing {raw_item}...")
        time.sleep(0.8) # Consumer is slow
        data_queue.task_done()

if __name__ == "__main__":
    # --- Start the Producer Threads ---
    producer_threads = []
    records_per_producer = TOTAL_RECORDS_TO_PRODUCE // NUM_PRODUCERS
    
    for i in range(NUM_PRODUCERS):
        start = i * records_per_producer + 1
        end = (i + 1) * records_per_producer
        # Ensure the last producer gets any remaining records
        if i == NUM_PRODUCERS - 1:
            end = TOTAL_RECORDS_TO_PRODUCE
            
        producer_thread = threading.Thread(target=raw_data_producer, args=(start, end))
        producer_thread.start()
        producer_threads.append(producer_thread)
    
    # --- Start the Consumer Threads ---
    consumer_threads = []
    for i in range(NUM_CONSUMERS):
        t = threading.Thread(target=data_consumer, args=(i,))
        t.start()
        consumer_threads.append(t)
        
    # --- Wait for all producers to finish adding items to the queue ---
    for t in producer_threads:
        t.join()
    
    # --- Wait for all items in the queue to be processed ---
    data_queue.join()
    
    # --- Stop the consumers by sending one sentinel value for each ---
    for _ in range(NUM_CONSUMERS):
        data_queue.put(None)
        
    # --- Wait for all consumer threads to finish shutting down ---
    for t in consumer_threads:
        t.join()
        
    print(f"✅ Entire pipeline finished successfully with {NUM_PRODUCERS} producer(s) and {NUM_CONSUMERS} consumer(s)!")
