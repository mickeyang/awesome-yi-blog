import time
from concurrent.futures import ProcessPoolExecutor

# A heavily intensive CPU task (counting to 50 million)
def heavy_cpu_math(chunk_id: int) -> int:
    total = 0
    for i in range(50_000_000):
        total += i
    return total + chunk_id

# The mandatory entry guard
if __name__ == "__main__":
    chunks = [1, 2, 3, 4]
    
    start_time = time.time()
    
    # ProcessPoolExecutor matches your hardware cores automatically if max_workers isn't set
    with ProcessPoolExecutor() as executor:
        results = executor.map(heavy_cpu_math, chunks)
        
    print(list(results))
    print(f"Executed parallel calculation in {time.time() - start_time:.2f} seconds")