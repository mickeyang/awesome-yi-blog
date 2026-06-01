from typing import Any

# TESTING DATA
valid_config = {"db_name": "analytics_db", "retry_count": 3, "environment": "PROD"}
invalid_config = {"db_name": "analytics_db", "retry_count": "three", "environment": "STAGE"}

def initialise_pipeline(config: dict[str, Any]) -> str:
    # 1. Check db_name safely using .get()
    db_name = config.get("db_name")
    if not isinstance(db_name, str):
        raise TypeError(f"Config 'db_name' must be a string. Got: {type(db_name).__name__}")
        
    # 2. Check retry_count (Added missing requirement)
    retry_count = config.get("retry_count")
    if not isinstance(retry_count, int):
        raise TypeError(f"Config 'retry_count' must be an integer. Got: {type(retry_count).__name__}")
        
    # 3. Check environment using single quotes inside the f-string
    environment = config.get("environment")
    if environment not in ["PROD", "DEV"]:
        raise ValueError(f"Config 'environment' must be 'PROD' or 'DEV'. Got: {environment}")
        
    # Alternating quotes prevents the SyntaxError
    return f"Connected to {db_name} in {environment} with {retry_count} retries."

# initialise_pipeline(valid_config)
# initialise_pipeline(invalid_config)

try:
    initialise_pipeline(invalid_config)
except (TypeError, ValueError) as e:
    print(f"Pipeline safely blocked! Error: {e}")
