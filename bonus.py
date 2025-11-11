import sys

if len(sys.argv) == 3:
    script_name = sys.argv[0]
    salary = float(sys.argv[1])
    bonus = float(sys.argv[2]) * 0.10
    print("User provided input values:")
    print("Script name:", script_name)
    print("Salary:", salary)
    total_salary = salary + bonus
    print("Total Salary:", total_salary)

else:
    script_name = sys.argv[0]
    salary = 10000.0
    bonus = salary * 0.10
    print("No input given:")
    print("Script name:", script_name)
    print("Default Salary:", salary)
    total_salary = salary + bonus
    print("Total Salary:", total_salary)
