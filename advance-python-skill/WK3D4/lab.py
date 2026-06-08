import time
import queue
import threading

pipeline_queue = queue.Queue()
raw_logs = ["ERROR_404_USER", "INFO_200_OK", "WARN_500_DB", "ERROR_403_AUTH", "INFO_201_CREATED", "WARN_408_TIME"]

def log_producer():
    for log in raw_logs:
        time.sleep(0.1) # Simulates rapid log ingestion
        # YOUR WORK HERE: Push 'log' into the pipeline_queue
        pipeline_queue.put(log)
        print(f"[PRODUCER] Ingested raw log: {log}")

def log_consumer(worker_name: str):
    while True:
        # YOUR WORK HERE: Grab an item from the pipeline_queue
        log_item = pipeline_queue.get() # Replace this with the queue call
        
        if log_item is None:
            # YOUR WORK HERE: Signal task done for the exit token
            pipeline_queue.task_done()
            break
            
        # Process the log
        severity = log_item.split("_")[0]
        print(f"[{worker_name}] Parsed event with severity: {severity}")
        time.sleep(0.3) # Simulates heavy string regex matching
        
        # YOUR WORK HERE: Signal task done for the processed log
        pipeline_queue.task_done()

if __name__ == "__main__":
    # 1. Spin up the Producer
    p = threading.Thread(target=log_producer)
    p.start()
    
    # 2. Spin up 2 Consumers
    consumers = []
    for name in ["Consumer_Alpha", "Consumer_Beta"]:
        c = threading.Thread(target=log_consumer, args=(name,))
        c.start()
        consumers.append(c)
        
    p.join()
    pipeline_queue.join()
    
    # Poison pill to shut down consumers
    for _ in range(2):
        pipeline_queue.put(None)
    for c in consumers:
        c.join()
        
    print("All logs categorized and securely parsed.")