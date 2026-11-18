# user inputs
item_name = input("Enter the item name: ").strip().lower()
starting_rolls = int(input("Enter the starting rolls: "))
rolls_used = int(input("Enter the rolls used: "))
reorder_point = int(input("Enter the reorder point: "))

# vars
remaining_rolls = 0

# boolean conditions
rejected_name = False
negative_number = False
exceeding_quant = False
good_to_go = False

# reject empty name and switch boolean flag
if item_name == "":
    rejected_name = True
    print("Item name cannot be blank.")
else:
    print(f"{item_name} was accepted as a valid name")

# reject negative number and switch boolean flag
if starting_rolls < 0 or rolls_used < 0 or reorder_point < 0:
    negative_number = True
    print("You supplied negative values")
else:
    print(f"Your values are:\nStarting rolls: {starting_rolls}\nRolls used: {rolls_used}\nReorder point: {reorder_point}")

# reject a used quantity greater than starting stock

if rolls_used > starting_rolls:
    exceeding_quant = True
    print("You have used more rolls than the starting amount.")

# checks to see if all values are good at once before executing the loop
if not rejected_name and not negative_number and not exceeding_quant:
    good_to_go = True

# Operations on valid inputs
if good_to_go:
    remaining_rolls = starting_rolls - rolls_used
    if remaining_rolls >= 0:
        print(f"You have {remaining_rolls} remaining rolls.")

# Prints status
if good_to_go and remaining_rolls == 0:
    print("OUT OF STOCK")
elif good_to_go and remaining_rolls <= reorder_point:
    print("REORDER")
elif good_to_go:
    print("STOCK OK")


