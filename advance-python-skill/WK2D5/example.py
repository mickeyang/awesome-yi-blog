# The actual pipeline transformation function
def clean_monetary_amount(raw_val: str | None) -> float:
    if raw_val is None or raw_val.strip() == "":
        return 0.0
    
    # Strip currency signs and commas, then cast to float
    cleaned = raw_val.replace("$", "").replace(",", "").strip()
    return float(cleaned)

# ==========================================
# THE AUTOMATED UNIT TEST SUITE
# ==========================================
def test_clean_monetary_amount():
    print("Running data transformation unit tests...")
    
    # Test Case 1: Standard clean data
    assert clean_monetary_amount("$1,250.50") == 1250.50
    
    # Test Case 2: Handle edge case missing data (Nulls)
    assert clean_monetary_amount(None) == 0.0
    
    # Test Case 3: Handle dirty whitespace strings
    assert clean_monetary_amount("   ") == 0.0
    
    print("All unit tests passed! Transformation logic is stable.")

# Run the test suite
test_clean_monetary_amount()