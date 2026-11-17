from salary import calculate_salary

def test_gross_salary():
    assert calculate_salary() == 65000

def test_salary_type():
    assert isinstance(calculate_salary(), (int, float))

def test_salary_positive():
    assert calculate_salary() > 0