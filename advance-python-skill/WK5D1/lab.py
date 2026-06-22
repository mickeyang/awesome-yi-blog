import cProfile
import pstats
import re

log_data = ["  [ERROR] USER_ID:102938 - Connection timed out after 30s   " for _ in range(100_000)]

# Fix: Compile ONCE at the module level
USER_ID_PATTERN = re.compile(r"user_id:(\d+)")

def clean_whitespace(text):
    return text.strip().lower()

def extract_user_id(text):
    # Now we just reference the pre-compiled object
    match = USER_ID_PATTERN.search(text)
    return match.group(1) if match else None

def heavy_pipeline(data):
    cleaned = [clean_whitespace(line) for line in data]
    user_ids = [extract_user_id(line) for line in cleaned]
    return user_ids

if __name__ == "__main__":
    profiler = cProfile.Profile()
    profiler.enable()
    
    results = heavy_pipeline(log_data)
    
    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats('tottime')
    stats.print_stats(10)