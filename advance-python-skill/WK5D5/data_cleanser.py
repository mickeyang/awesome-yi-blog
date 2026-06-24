import re

DEPT_PATTERN = re.compile(r"dept:([a-z]+)")

def extract_department(log_line: str) -> str:
    """
    Extracts the department name. Returns 'unknown' if missing or invalid.
    """
    if not log_line or not isinstance(log_line, str):
        return "unknown"
        
    match = DEPT_PATTERN.search(log_line.lower())
    return match.group(1) if match else "unknown"