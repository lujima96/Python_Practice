# F string allow insertion of values directly into a string
item_name = "Label Roll"
quantity = 210

# f before the opening quote enables this formatting. Python evaluates what's iunside {} and inserts value
print(f"Rolls available: {quantity}")

print(f"There are {quantity} {item_name}s available.")

# Without the f the braces remain literal text

print("There are {quantity} {item_name}s available")

# Decimal formatting control

weight = 7.5018976

print(f"Weight: {weight:.2f} kg")
