"""
Task 8 — Movie Ratings Dashboard 📊

Requirements:
  - ratings = [4, 5, 3, 2, 5, 4, 5, 3, 4]
  - Use a loop to compute:
      * Average rating (1 decimal)
      * Count of 5-star reviews
  - Print both results on separate lines

Practice: loop aggregation, counting, formatting

OUTPUT EXAMPLE
--------------
Average rating: 3.9
Number of 5-star reviews: 3
"""

ratings = [4, 5, 3, 2, 5, 4, 5, 3, 4]
print("(Starter) Ratings:", ratings)
print(f"Average rating: {round(sum(ratings)/len(ratings), 1)}\nNumber of 5-star reviews: {ratings.count(5)}")


