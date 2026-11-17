### Guided Lessons

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

# Cleaning strings
item_name = "  Label Roll  "

## White Space Strip
print(item_name.strip())

### Lower Case
print(item_name.lower())

# These methods return new strings but do not automatically change the variable

car_make = "  Toyota  "
car_make.strip()
print("Make:", car_make)

# To keep the results you need to assign it to a variable

car_make = car_make.strip()
print("Make:", car_make)

# You can combine methods for cleaning

car_make = input("Enter your car make:").strip().lower()
print(car_make)

item_name = input("Item name: ".strip())
package_count = int(input("Number of packages: "))
weight_per_package = float(input("Weight of each package: "))

total_weight = package_count * weight_per_package

print()
print(f"Item: {item_name}")
print(f"Packages: {package_count}")
print(f"Total weight: {total_weight}")

### Independant practice

# Error Code
# -------------------------------------------------------#
# quantity = input("Quantity available: ")
# remaining = quantity - 3

# print(f"Remaining: {remaining}")
# -------------------------------------------------------#

# The error stems from a string being assigned to quantity and then trying to perform a math operation on the wrong data type
## Corrected code

quantity = int(input("Quantity available: "))
remaining = quantity - 3

print(f"Remaining: {remaining}")

# Program prompt

# Write a program that asks for:

# Item name
# Number of boxes
# Rolls per box
# Rolls used

# The program should:

# Remove surrounding whitespace from the item name
# Convert the three counts to integers
# Calculate starting rolls and remaining rolls
# Print a readable report using f-strings

# Inputs for the run:
# Shipping labels
# 8 
# 20
# 13

item_name = input("Enter the item name.").strip()
number_of_boxes = int(input("Enter the number of boxes."))
rolls_per_box = int(input("Enter the number of rolls per box."))
rolls_used = int(input("Enter the number of rolls used."))

starting_rolls = number_of_boxes * rolls_per_box
remaining_rolls = starting_rolls - rolls_used

print(f"Starting rolls: {starting_rolls}\nRemaining rolls: {remaining_rolls}")

# Assigns '  PACKAGING  ' to category
category = "  PACKAGING  "

# Strips the white space to the left and right turning category to 'Packaging'
category.strip()

# f string printing 'Category: [PACKAGING]
## Error was made in this prediction. The stripped 'PACKAGING' was not assigned to the var at this time yet
print(f"Category: [{category}]")

# Performs both a strip and a lower case operation on category
## This is where it is actualy assigned
category = category.strip().lower()

# f string printing 'Category: [packaging]'
print(f"Category: [{category}]")

# Predict the output 

# boxes assigned string value of '6'
boxes = "6"
# rolls_per_box assigned string value of '24'
rolls_per_box = "24"

# Concatenates to 624
print(boxes + rolls_per_box)

#Int conversion for both strings then multiplied together 6 * 24 = 144
print(int(boxes) * int(rolls_per_box))

# Prints value assigned to boxes within an f string. Output 'Boxes: 6'
print(f"Boxes: {boxes}")

# F string not used. Expected output 'Boxes: {boxes}'
print("Boxes: {boxes}")

# Write a program that asks for a topic and a target audience, then prints:
# Explain networking to restaurant managers using a practical example.
# Optionally add a character count
topic = str(input("Enter your chosen topic: "))
target_audience = str(input("Enter your target audience: "))

prompt = f"Explain {topic} to {target_audience} using a practical example."
character_count = len(prompt)

print(f"{prompt}\nCharacter count: {character_count}")