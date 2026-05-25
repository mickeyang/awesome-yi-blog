mock_raw_logs = [
    "INFO: User logged in",
    "ERROR: Database connection timeout",
    "DEBUG: Query executed in 0.02s",
    "ERROR: Out of memory in container 4",
    "INFO: Report exported successfully"
]

def parse_log_generator(log_file):
    for line in log_file:
        log_level, log_content = line.split(":", 1)  # stop split at the first colon
        if log_level == "ERROR":
            yield {
                "level" : log_level, 
                "message": log_content
            }

log_stream = parse_log_generator(mock_raw_logs)
for log_entry in log_stream:
    print(f"Successfully processed: {log_entry['message']}")

