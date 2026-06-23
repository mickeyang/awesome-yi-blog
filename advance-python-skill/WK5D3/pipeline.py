import re

USER_ID_PATTERN = re.compile(r"user_id:(\d+)")

class LogFetcher:
    def __init__(self, client):
        self.client = client  # This will be our fake client during testing

    def fetch_raw_logs(self, bucket_name: str) -> list:
        # Chained call: client -> get_object() -> dict lookup -> read() -> decode() -> splitlines()
        response = self.client.get_object(Bucket=bucket_name)
        return response["Body"].read().decode('utf-8').splitlines()

def clean_and_extract(raw_logs: list) -> list:
    extracted = []
    for line in raw_logs:
        cleaned = line.strip().lower()
        match = USER_ID_PATTERN.search(cleaned)
        if match:
            extracted.append(match.group(1))
    return extracted