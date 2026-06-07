import time
from concurrent.futures import ThreadPoolExecutor, as_completed

target_urls = ["api/v1/users", "api/v1/orders", "api/v1/products", "api/v1/metrics", "api/v1/logs"]

def simulate_download(url: str) -> str:
    # Simulates waiting 1 second for a server network response
    time.sleep(1)
    return f"Successfully downloaded data from {url}"

# YOUR WORK HERE: 
# Implement the ThreadPoolExecutor to run simulate_download on all target_urls concurrently.
# Print the results as they finish.

# with ThreadPoolExecutor(max_workers=5) as executor:
#     iterators = executor.map(simulate_download, target_urls)
#     for i in iterators:
#         print(i)

with ThreadPoolExecutor(max_workers=5) as executor:
    # Submit returns a dictionary of Future objects
    futures = {executor.submit(simulate_download, url): url for url in target_urls}
    
# as_completed yields them dynamically as they cross the finish line
for future in as_completed(futures):
    result = future.result()
    print(result)