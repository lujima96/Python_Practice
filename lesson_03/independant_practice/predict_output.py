
# Remaining rolls assigned value of 5
remaining_rolls = 5
# Reorder point set to 5
reorder_point = 5

# needs reorder evaluates to true because remaining rolls is = to reorder point
needs_reorder = remaining_rolls <= reorder_point
# is empty evaluates to false because remaining rolls is not equal to 0
is_empty = remaining_rolls == 0

# prints True
print(needs_reorder)
# prints False
print(is_empty)
# prints True because not flips is_empty to true, both conditions satisfy
print(needs_reorder and not is_empty)

# First if chain does not execute because the condition is not satisfied
if is_empty:
    print("OUT OF STOCK")
#REORDER is printed because the condition is true
elif needs_reorder:
    print("REORDER")
#Never executes because the previous statement was satisfied
else:
    print("STOCK OK")