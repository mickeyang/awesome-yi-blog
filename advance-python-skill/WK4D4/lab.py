import os
import shutil # 
import pyarrow as pa
import pyarrow.parquet as pq
import pyarrow.dataset as ds # managing data changes

# Prepare a clean directory for our evolving data lake
lake_dir = "advance-python-skill/WK4D4/evolving_lake"
if os.path.exists(lake_dir):
    shutil.rmtree(lake_dir)
os.makedirs(lake_dir)

# --- SIMULATING THE PAST (2025) ---
# Old application layout: Just ID and Amount
v1_table = pa.table({
    "order_id": [1001, 1002],
    "amount": [50.50, 99.99]
})
pq.write_table(v1_table, os.path.join(lake_dir, "data_2025.parquet"))

# --- SIMULATING THE PRESENT (2026) ---
# New application layout: A new 'promo_code' column is introduced!
v2_table = pa.table({
    "order_id": [1003, 1004],
    "amount": [120.00, 15.00],
    "promo_code": ["SAVE10", "FREESHIP"] # Added column
})
pq.write_table(v2_table, os.path.join(lake_dir, "data_2026.parquet"))

# 1. YOUR WORK HERE: Use pyarrow.dataset (imported as 'ds') to read the entire 'evolving_lake' directory.
# This engine automatically scans all file footers to resolve schema drifts.
base_dataset = ds.dataset(lake_dir, format="parquet")

# Extract and merge the schemas from all files inside the directory
all_schemas = [fragment.physical_schema for fragment in base_dataset.get_fragments()]
unified_schema = pa.unify_schemas(all_schemas)

# 2. Compile the dataset into a single unified table view
# YOUR WORK HERE: Call the appropriate method on the dataset object to convert it to a full table
unified_table = ds.dataset(lake_dir, format="parquet", schema=unified_schema).to_table()

print("📊 Unified Evolved Dataset Results:")
print(unified_table.to_pydict())
