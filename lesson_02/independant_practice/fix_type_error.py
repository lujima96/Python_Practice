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