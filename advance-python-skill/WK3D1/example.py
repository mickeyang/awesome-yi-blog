import requests

# SCENARIO A: I/O-Bound (Waiting for the internet)
def fetch_api_status():
    # The CPU does nothing for 99% of this function's life; it just waits on the network.
    response = requests.get("https://api.github.com")
    return response.status_code

# SCENARIO B: CPU-Bound (Slamming the processor)
def crunch_massive_numbers():
    # The CPU is working at 100% capacity calculating this loop.
    total = 0
    for i in range(10_000_000):
        total += i * i
    return total