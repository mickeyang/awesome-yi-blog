import pytest
from data_cleanser import extract_department

# We define the variable names as a string, then pass a list of test cases
@pytest.mark.parametrize(
    "test_input, expected_output",
    [
        ("2026-06-24 INFO dept:finance transaction_id:993", "finance"),  # Happy path
        ("2026-06-24 ERROR dept:HR system_failure", "hr"),             # Case insensitivity check
        ("Malformed log line with no department mentioned", "unknown"), # Missing data check
        ("", "unknown"),                                               # Empty string check
        (None, "unknown"),                                             # NoneType safety check
        (12345, "unknown"),                                            # Corrupt data type check
    ]
)
def test_extract_department_across_various_inputs(test_input, expected_output):
    """
    Pytest will run this exact function 6 separate times, swapping out
    test_input and expected_output automatically for each case.
    """
    # Act
    actual_result = extract_department(test_input)
    
    # Assert
    assert actual_result == expected_output