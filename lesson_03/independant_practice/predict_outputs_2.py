# Both if statements are independant and both are true so Low Stock and Out of stock are printed

remaining_rolls = 0

if remaining_rolls <= 10:
    print("Low stock")

if remaining_rolls == 0:
    print("Out of stock")

remaining_rolls = 0

# First condition evaluates true so Low Stock prints and the remaining code doesn't run.
if remaining_rolls <= 10:
    print("Low stock")
elif remaining_rolls == 0:
    print("Out of stock")

#Expected output
# Low stock, Out of stock, Low stock