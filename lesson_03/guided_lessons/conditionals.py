# if block allows you to run code conditionally
#
# if introduces the condition
# : ends the condition line
# indentation identifies the instructions belonging to that condition
# python best practice is to use 4 spaces for indentation

remaining_rolls = 8

if remaining_rolls <= 10:
    print("Reorder needed.")

print("Inventory check completed.")

# else and if

remaining_rolls = 18

if remaining_rolls <= 10:
    print("Reorder needed.")
else:
    print("Stock level is sufficient.")

# elif

remaining_rolls = 0

if remaining_rolls == 0:
    print("Out of stock!")
elif remaining_rolls <= 10:
    print("Reorder")
else: print("Stock ok")

# Independant if statements behave differently

remaining_rolls = 1

if remaining_rolls <= 10:
    print("Reorder needed.")

if remaining_rolls == 1:
    print("Last roll.")