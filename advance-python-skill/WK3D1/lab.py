import time
from concurrent.futures import ThreadPoolExecutor, as_completed

target_urls = ["api/v1/users", "api/v1/orders", "api/v1/products", "api/v1/metrics", "api/v1/logs"]

def simulate_download(url: str) -> str:
    # Simulates waiting 1 second for a server network response
    if(url == "api/v1/orders"):
        time.sleep(1.5)
    time.sleep(1)
    return f"Successfully downloaded data from {url}"

# WITHOUT CONCURRENCY
start_time = time.time()
for t in target_urls:
    simulate_download(t)
end_time = time.time()
print(f"The whole process took {end_time - start_time:.2f} seconds") # 8 seconds

# YOUR WORK HERE: 
# Implement the ThreadPoolExecutor to run simulate_download on all target_urls concurrently.
# Print the results as they finish.

# WITH CONCURRENCY executor, this approach must follow the target_urls order
start_time = time.time()
with ThreadPoolExecutor(max_workers=5) as executor:
    iterators = executor.map(simulate_download, target_urls)
    for i in iterators:
        print(i)
end_time = time.time()
print(f"The whole process took {end_time - start_time:.2f} seconds") # 8 seconds
print(f"The target url list is: {target_urls}")

# WITH CONCURRENCY executor + futures, this approach does not need to follow the target_urls order
# once finish, then print out result
start_time = time.time()
with ThreadPoolExecutor(max_workers=5) as executor:
    # Submit returns a dictionary of Future objects
    futures = {executor.submit(simulate_download, url): url for url in target_urls}
# as_completed yields them dynamically as they cross the finish line
for future in as_completed(futures):
    result = future.result()
    print(result)
end_time = time.time()
print(f"The whole process took {end_time - start_time:.2f} seconds") # 8 seconds
print(f"The target url list is: {target_urls}")
