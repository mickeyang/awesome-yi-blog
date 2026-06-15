import os
import pyarrow as pa
import pyarrow.parquet as pq

# Raw ecommerce dataset
mock_sales_table = pa.table({
    "order_id": [1001, 1002, 1003, 1004],
    "amount": [250.00, 45.50, 1200.00, 89.99],
    "year": [2025, 2025, 2026, 2026],
    "country": ["US", "CA", "US", "UK"]
})

# --- YOUR WORK STARTS HERE ---

# 1. YOUR WORK HERE: Export the table to a directory named "ecommerce_lake", 
# partitioning the files by the "country" column.
pq.write_to_dataset(
    mock_sales_table, 
    root_path = "advance-python-skill/WK4D3/ecommerce_lake",
    partition_cols = ["country"]
    )

# 2. Automatically inspect the generated directories
print("📁 Generated Directory Structure:")
for root, dirs, files in os.walk("advance-python-skill/WK4D3/ecommerce_lake"):
    level = root.replace("ecommerce_lake", "").count(os.sep)
    indent = " " * 4 * (level)
    print(f"{indent}{os.path.basename(root)}/")
    subindent = " " * 4 * (level + 1)
    for f in files:
        print(f"{subindent}{f}")
