import time
import threading
from concurrent.futures import ThreadPoolExecutor

# YOUR WORK HERE: Instantiate your lock here
safe_locker = threading.Lock()
FILE_NAME = r"advance-python-skill/WK3D3/error_pipeline.log"

def thread_safe_writer(thread_id: int) -> None:
    message = f"Error detected by Thread-{thread_id} at system checkpoint.\n"
    
    # YOUR WORK HERE: 
    # Secure this block with your lock so threads don't overwrite each other's file writes.
    with safe_locker:
        with open(FILE_NAME, "a") as f:
            f.write(message)
            time.sleep(0.01) # Simulates file disk latency

if __name__ == "__main__":
    # Clear out previous logs if they exist
    open(FILE_NAME, "w").close()
    
    # Spin up 20 threads trying to write to the file simultaneously
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(thread_safe_writer, range(20))
        
    # Read and count the total written lines
    with open(FILE_NAME, "r") as f:
        lines = f.readlines()
        
    print(f"Total lines written successfully: {len(lines)}/20")