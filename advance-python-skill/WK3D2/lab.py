import time
from concurrent.futures import ProcessPoolExecutor
import random

# Mock data chunks representing massive rows of text data
data_chunks = [
    "LOG_DATA_STREAM_PART_A" * 100_000,
    "LOG_DATA_STREAM_PART_B" * 100_000,
    "LOG_DATA_STREAM_PART_C" * 100_000,
    "LOG_DATA_STREAM_PART_D" * 100_000
]

def CPU_intensive_parse(chunk: str) -> int:
    # Simulates heavy processing by forcing millions of string transformations
    counter = 0
    for char in chunk:
        if char == "A":
            counter += 1
    return counter

# If you run this function through your two setups:
def brutal_cpu_math(chunk: str) -> int:
    counter = 0
    # Forcing the CPU to calculate heavy math over and over
    for i in range(5_000_000):
        counter += (i ** 2) // 3 * random.random()
    return counter

# YOUR WORK HERE:
# Implement the ProcessPoolExecutor block inside the proper entry guard.
# Print the results of the parsed character counts.
if __name__ == "__main__":
    start_time = time.time()
    with ProcessPoolExecutor() as executor:
        # results = executor.map(CPU_intensive_parse, data_chunks)
        results = executor.map(brutal_cpu_math, data_chunks)
    # for r in results:
    #     print(f"There are {r} occurrences.")
    end_time = time.time()
    print(f"[WITH ProcessPoolExecutor] - The whole process took {end_time - start_time:.2f} seconds") # 3.42 seconds

# WHAT-IF without the ProcessPoolExecutor()
# start_time = time.time()
# for d in data_chunks:
#     brutal_cpu_math(d)
#     # print(CPU_intensive_parse(d))
#     # print(brutal_cpu_math(d))
# end_time = time.time()
# print(f"[WITHOUT ProcessPoolExecutor] - The whole process took {end_time - start_time:.2f} seconds") # 8.49 seconds