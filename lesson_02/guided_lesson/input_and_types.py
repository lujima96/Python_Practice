# Taking user input
item_name = input("Enter the item name: ")
print("You entered:", item_name)

# Type Checking
print(type("12"))
print(type(12))
print(type(12.5))

# Type Checking Variable
print(type(item_name))

# Input returns text, even when someone types digits
quantity_text = input("How many rolls?")
print(quantity_text + quantity_text)

# Convert inputs into integers
quantity = int(quantity_text)
print(quantity + quantity)

# Combined for brevity
quantity_combined = input("How many rolls?")
quantity = int(quantity_combined)
print(type(quantity))

# Decimal measurements use floats

weight_kg = float(input("Enter your weight in kilograms: "))
print("Double that weight: ", weight_kg * 2)

# Conversions require suitable input
## These work
int("12")
float("2.5")
float("12")

### These raise a value error
int("twelve")
int("2.5")
float("heavy")