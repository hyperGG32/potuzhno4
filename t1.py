"""
Task 1 — Shopping Cart Tracker 🛒

Real-world context:
  A POS app keeps a shopping cart as a Python list.

Requirements:
  1) Start with cart = ["milk", "bread", "eggs", "apples", "coffee"].
  2) Print each item for a receipt using a for-loop (numbered lines).
  3) Add two items: "cheese" and "butter".
  4) Print the updated cart on one line (comma-separated).

Practice: lists, for-loops, enumerate, str.join

OUTPUT EXAMPLE
--------------
Receipt items:
1. milk
2. bread
3. eggs
4. apples
5. coffee

Updated cart: milk, bread, eggs, apples, coffee, cheese, butter
"""

cart = ["milk", "bread", "eggs", "apples", "coffee"]

print("(Starter) Initial cart:", cart)

for i, e in enumerate(cart):
    print(i + 1, e, sep=". ")

cart.extend(["cheese", "butter"])
print("Updated cart:", end=' ')
for e in cart:
    if e == cart[-1]:
        print(e, end='.')
        break
    print(e, end=', ')
