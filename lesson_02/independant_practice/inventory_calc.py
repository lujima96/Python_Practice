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
print(item_name)
print(f"Starting rolls: {starting_rolls}\nRemaining rolls: {remaining_rolls}")