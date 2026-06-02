import logging
# logging.basicConfig(
#     format="%(asctime)s [%(levelname)s] %(message)s",
#     level = logging.INFO
# )
logger = logging.getLogger("dual_logger")
logger.setLevel(logging.INFO)
formatter = logging.Formatter(
    fmt="%(asctime)s [%(levelname)s] %(message)s"
)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
console_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler(filename="advance-python-skill/WK2D3/production_logging.log", mode="a")
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.WARNING)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Raw starter code to fix:
def process_batch(batch_id, data):
    logger.info(f"Starting batch {batch_id}")
    if not data:
        logger.warning("Empty data received! Skipping batch.") # Replace me
        return
    try:
        for item in data:
            if item == "corrupt":
                raise ValueError("Corrupt record detected!")
        logger.info(f"Batch {batch_id} completed successfully.")
    except Exception:
        logger.exception(f"Batch {batch_id} failed during execution.")

# TESTING DATA
# Mock executions to run after your setup:
process_batch(1, ["valid_row_1", "valid_row_2"])
process_batch(2, [])
process_batch(3, ["valid_row_1", "corrupt"])
