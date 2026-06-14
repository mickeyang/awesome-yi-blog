import os
import pyarrow as pa
import pyarrow.parquet as pq

# The raw data data blocks
statuses_unsorted = ["SUCCESS", "FAILED", "SUCCESS", "SUCCESS", "PENDING", "FAILED"] * 50_000
ids_unsorted = [101, 505, 101, 101, 303, 505] * 50_000

# 1. YOUR WORK HERE: Create sorted versions of these lists 
# so identical values are grouped together consecutively.
statuses_sorted = sorted(statuses_unsorted)
ids_sorted = sorted(ids_unsorted)

# Create the PyArrow Tables
table_unsorted = pa.table({"status": statuses_unsorted, "id": ids_unsorted})
table_sorted = pa.table({"status": statuses_sorted, "id": ids_sorted})

# Write them to disk with compression enabled
pq.write_table(table_unsorted, "data_unsorted.parquet", compression="snappy")
pq.write_table(table_sorted, "data_sorted.parquet", compression="snappy")

# Get file sizes in bytes
size_unsorted = os.path.getsize("data_unsorted.parquet")
size_sorted = os.path.getsize("data_sorted.parquet")

print(f"📦 Unsorted Parquet Size: {size_unsorted:,} bytes")
print(f"🗜️ Sorted Parquet Size:   {size_sorted:,} bytes")

# Calculate the difference percentage
reduction = ((size_unsorted - size_sorted) / size_unsorted) * 100
print(f"🔥 Sorting achieved a {reduction:.2f}% storage reduction!")
