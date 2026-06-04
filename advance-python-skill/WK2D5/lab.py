def calculate_tax_and_total(price: float, tax_rate: float) -> dict:
    # if price < 0 or tax_rate < 0:
    #     raise ValueError("Price and tax rate must be non-negative values.")
        
    tax_amount = round(price * tax_rate, 2)
    total_amount = round(price + tax_amount, 2)
    
    return {"tax": tax_amount, "total": total_amount}

def run_pipeline_test_suite():
    print("Start unit testing...")
    # UNIT TESTING CASE 1
    assert calculate_tax_and_total(100.0, 0.10) == {"tax": 10.0, "total": 110.0}

    # UNIT TESTING CASE 2
    assert calculate_tax_and_total(price=0.0, tax_rate=0.10) == {"tax": 0.0, "total": 0.0}

    # UNIT TESTING CASE 3
    error_triggered = False
    try:
        calculate_tax_and_total(price=-50.0, tax_rate=0.10)
    except ValueError as e:
        error_triggered = True
        assert str(e) == "Price and tax rate must be non-negative values."

    assert error_triggered, "Security Flaw: Function failed to raise ValueError on a negative price!"

    print("All unit testing passed...")

run_pipeline_test_suite()
