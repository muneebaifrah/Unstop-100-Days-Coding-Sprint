# Read inputs
N = int(input().strip())  # Initial balance
M = int(input().strip())  # Number of employees
employees = input().strip().split()  # Employee names (not used in logic)
salaries = list(map(int, input().strip().split()))

results = []
balance = N

for salary in salaries:
    if salary <= balance:
        results.append("true")
        balance -= salary
    else:
        results.append("false")

print(" ".join(results))