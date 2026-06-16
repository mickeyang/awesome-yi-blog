import duckdb
import pyarrow as pa
import pyarrow.parquet as pq

# Setting up the raw mock telemetry data
telemetry_table = pa.table({
    "component": ["AUTH", "DB_WRITE", "AUTH", "API_GATEWAY", "AUTH", "DB_WRITE"],
    "execution_time_ms": [120.5, 450.2, 95.0, 15.3, 110.1, 380.9],
    "status": ["200", "201", "500", "200", "200", "200"]
})
pq.write_table(telemetry_table, "advance-python-skill/WK4D5/system_telemetry.parquet")

# --- YOUR WORK STARTS HERE ---

# YOUR WORK HERE: Write the SQL statement inside the triple quotes.
# Target file: 'system_telemetry.parquet'
sql_query = """
    SELECT 
        component,
        avg(execution_time_ms) as average_exec_time
    FROM 'advance-python-skill/WK4D5/system_telemetry.parquet'
    WHERE component = 'AUTH'
    GROUP BY component
"""

# Execute the query using DuckDB and convert to a Pandas DataFrame
report_df = duckdb.query(sql_query).to_df()

print("📊 Telemetry Performance Report:")
print(report_df)
