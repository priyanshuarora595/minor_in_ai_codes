def highest_salary_per_employee(employees_salaries):
    result = {}
    for employee, salaries in employees_salaries.items():
        result[employee] = max(salaries)
    return result
