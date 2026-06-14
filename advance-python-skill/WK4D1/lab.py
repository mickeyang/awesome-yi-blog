import pyarrow as pa
import pyarrow.parquet as pq

# Mocking up a sample dataset
mock_table = pa.table({
    "user_id": [101, 102, 103],
    "event_type": ["click", "purchase", "scroll"],
    "ip_address": ["192.168.1.1", "10.0.0.5", "172.16.0.2"],
    "raw_user_agent_string": ["Mozilla/5.0..." * 50, "Safari/537..." * 50, "Chrome/114..." * 50]
})
# Save it as a Parquet file on disk
pq.write_table(mock_table, "analytics_stream.parquet")

# --- YOUR WORK STARTS HERE ---

# 1. Read the schema metadata without loading the file's records
parquet_file = pq.ParquetFile("analytics_stream.parquet")
print("Parquet Schema Metadata:")
print(parquet_file.schema)

# 2. Extract ONLY 'user_id' and 'event_type' cleanly from disk
# YOUR WORK HERE: Add the correct argument to read_table to limit column read
optimized_table = pq.read_table("analytics_stream.parquet", columns=["user_id", "event_type"]) 

# Convert to a dictionary to view results
print("Optimized Extracted Data:")
print(optimized_table.to_pydict())
