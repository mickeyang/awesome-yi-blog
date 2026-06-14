import time
from concurrent.futures import ThreadPoolExecutor

file_ids = ["FILE_A", "FILE_BAD", "FILE_C"]

def defensive_downloader(file_id: str) -> str:
    if file_id == "FILE_BAD":
        print(f"{file_id} encountered a corruption error!")
        raise RuntimeError("CRITICAL: Download stream corrupted.")
        
    time.sleep(0.5)
    return f"Downloaded {file_id} successfully."

# YOUR WORK HERE:
# 1. Open a try/except block to intercept the RuntimeError.
# 2. Inside the try block, use ThreadPoolExecutor() as a context manager to map the downloader.
# 3. Print the results and catch the error loudly.

if __name__ == "__main__":
    
    try:
        with ThreadPoolExecutor() as executor:
            results_generator = executor.map(defensive_downloader, file_ids)
            results = list(results_generator)
            print(results)
    except RuntimeError as e:
        print(f"There is an error: {e}")
    
    print("System status: Context exited. All background threads safely reaped.")