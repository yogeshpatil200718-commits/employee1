def calculate_salary():
    basic_salary = 50000
    hra = basic_salary * 0.20
    da = basic_salary * 0.10
    gross_salary = basic_salary + hra + da
    return gross_salary

if __name__ == "__main__":
    print("Gross Salary:", calculate_salary())