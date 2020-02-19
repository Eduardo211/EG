# You work in a company with a starting salary of $70000
# You are told you will get a 2% merit raise for your salary
# Write a program with a loop that displays the projected salary
# for the next 5 years
NUMBER_YEAR = 5
SALARY = 70000
RAISE_RATE = 0.02
# Questions to ask yourself:
# 1. What type of loop do I use? A "while" loop or a "for" loop, why?
# 2. What is the mathematical equation for calculating
# the salary after the 2% raise?
# salary = salary + salary * 0.02

print("Year\t\tSalary")
for year in range(1,NUMBER_YEAR+1):
    SALARY = SALARY + SALARY * RAISE_RATE
    print(year,'\t\t',SALARY)