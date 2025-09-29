"""
Task 6 — Warehouse Stock Update 🏭

Requirements:
  - inventory = [["laptops", 15], ["keyboards", 40], ["mice", 30]]
  - A customer buys 3 keyboards
  - Use a loop to find "keyboards" and decrease quantity (not below 0)
  - Print old and new quantity

Practice: lists of lists, searching, in-place mutation

OUTPUT EXAMPLE
--------------
Inventory: [['laptops', 15], ['keyboards', 37], ['mice', 30]]
keyboards: 40 -> 37
"""
import sys

inventory = [["laptops", 15], ["keyboards", 40], ["mice", 30]]
keyb_old = inventory[1][1]
print("(Starter) Inventory:", inventory)

for i in inventory:
    if i[0] == ("keyboards"):
        if i[1] - 3 >= 0:
            i[1] -= 3
        else:
            print("Out of stock :(")
            sys.exit(67)

print("New inventory:", inventory)
print(f"Keyboards: {keyb_old} -> {inventory[1][1]}")