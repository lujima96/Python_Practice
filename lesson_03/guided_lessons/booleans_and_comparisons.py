# Booleans represent True and False
is_available = True
is_damaged = False

print(is_available)
print(type(is_available))

# Comparisons ask questions about values and produce boolean results
remaining_rolls = 8

print(remaining_rolls < 10)
print(remaining_rolls == 0)

# Comparison Operators
# == Equal to
# != Not equal to
# < Less than
# > greater than
# <= Less than OR equal to
# >= Greater than OR equal to

## Assignment and comparison using different operations
### NOTE: = assigns a value == compares values for equality
needs_reorder = remaining_rolls <= 10
print(needs_reorder)

# Types still matter for boolean expressions
## Type error will raise with a comparison of two different types
print("8" == 8)
print(int("8") == 8)

# String comparisons are case sensitive
category = "Packaging"
print(category == "packaging")
print(category.lower() == "packaging")

# When accepting user-entered text you want to compare consistently

category = input("Category: ").strip().lower()
print(category == "packaging")