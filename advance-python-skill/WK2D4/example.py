import time
import random
import logging

logger = logging.getLogger("resilient_pipeline")

def fetch_data_from_unstable_api():
    # Simulating a chaotic network connection
    if random.random() > 0.2:  # 80% chance to fail
        raise ConnectionResetError("Remote server closed connection unexpectedly.")
    return {"status": "success", "data": [1, 2, 3]}

def extract_with_retry(max_retries=3, base_delay=2):
    for attempt in range(1, max_retries + 1):
        try:
            logger.info(f"Attempt {attempt}/{max_retries}: Fetching data...")
            return fetch_data_from_unstable_api()
            
        except ConnectionResetError as e:
            if attempt == max_retries:
                logger.critical("Max retries reached. Pipeline execution aborted.")
                raise e  # Let it finally fail if it's completely dead
                
            # Calculate exponential backoff: base_delay * (2 ^ attempt)
            # Add "jitter" (a tiny random decimal) so parallel workers don't sync up
            delay = (base_delay ** attempt) + random.uniform(0, 1)
            
            logger.warning(f"Transient error detected: {e}. Retrying in {delay:.2f} seconds...")
            time.sleep(delay)

extract_with_retry()