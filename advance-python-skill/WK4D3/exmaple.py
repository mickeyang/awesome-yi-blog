import pyarrow as pa
import pyarrow.parquet as pq

# A sample dataset of system logs across different servers
table = pa.table({
    "timestamp": ["2026-06-15", "2026-06-15", "2026-06-16", "2026-06-16"],
    "server_id": ["Alpha", "Beta", "Alpha", "Beta"],
    "cpu_utilization": [85.2, 43.1, 88.9, 41.2]
})

# Write the table to disk partitioned by 'server_id'
pq.write_to_dataset(
    table,
    root_path="advance-python-skill/WK4D3/log_lake",
    partition_cols=["server_id"]
)
