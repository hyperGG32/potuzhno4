"""
Task 7 — ATM Cash Dispenser 🔢

Requirements:
  - bills = [100, 50, 20, 10]
  - For amount = 180, calculate greedy breakdown
  - Print like: "1x100, 1x50, 1x20, 1x10"
  - If not divisible by 10, print an error message

Practice: loops, integer division, modulo, conditional handling

OUTPUT EXAMPLE
--------------
1x100, 1x50, 1x20, 1x10
"""
import sys

amount = 180
bills = [100, 50, 20, 10]
print(f"(Starter) Amount: {amount}, Bills: {bills}")

if amount % bills[-1] != 0:
    print("ERROR!")
    sys.exit(1)
k = 0
while True:
    if amount >= bills[k]:
        if k == len(bills) - 1:
            print(f"{amount // bills[k]}x{bills[k]}")
        else:
            print(f"{amount//bills[k]}x{bills[k]}", end=', ')
        amount %= bills[k]
    else:
        k += 1
    if k == len(bills):
        break