import sys
if len(sys.argv) == 3:
  script_name = sys.argv[0]
  salary = float(sys.argv[1])
  bonus = float(sys.argv[2])*0.10
  print("user provided input values:")
  print("script name:", script_name)
  print("salary:", salary)
  totalsalary = bonus + salary
  
  print("total salary :",totalsalary)
else:
  script_name = sys.argv[0]
  salary = "1000"
  bonus = "10000 * 0.10"
  print("no input given:")
  print("script name:", script_name)
  print("salary:", salary)
  totalsalary = bonus + salary
  
  print("total salary:",totalsalary)
