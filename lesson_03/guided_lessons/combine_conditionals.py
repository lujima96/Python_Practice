# Conditionals can be combined with and, or, and not
#
# --and-- Both conditions must be true
# --or-- At least one condition needs to be true
# --not-- Reverses a Boolean result

remaining_rolls = 6
reorder_point = 10

# and
if remaining_rolls > 0 and remaining_rolls <= reorder_point:
    print("Low stock, but some rolls remain.")

# or
boxes = -2
rolls_used = 5

if boxes < 0 or rolls_used < 0:
    print("Quantities cannot be negative.")

# not
is_damaged = False

if not is_damaged:
    print("No damage reported.")

# Parentheses help keep expressions explicit and readable

is_admin = False
is_owner = True
is_locked = True

if(is_admin or is_owner) and not is_locked:
    print("Editing allowed.")
else:
    print("Editing not allowed.")


# When using -- or -- the subsequent conditions also need ==
priority = "urgent"

if priority == "urgent" or priority == "high":
    print("Prioritize this request.")