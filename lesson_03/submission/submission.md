### Guided Lessons

#### guided_lessons/booleans_and_comparisons.py

```python
# Booleans represent True and False
is_available = True
is_damaged = False

print(is_available)
print(type(is_available))

# Comparisons ask questions about values and produce boolean results
remaining_rolls = 8

print(remaining_rolls < 10)
print(remaining_rolls == 0)

# Comparison Operators
# == Equal to
# != Not equal to
# < Less than
# > greater than
# <= Less than OR equal to
# >= Greater than OR equal to

## Assignment and comparison using different operations
### NOTE: = assigns a value == compares values for equality
needs_reorder = remaining_rolls <= 10
print(needs_reorder)

# Types still matter for boolean expressions
## Type error will raise with a comparison of two different types
print("8" == 8)
print(int("8") == 8)

# String comparisons are case sensitive
category = "Packaging"
print(category == "packaging")
print(category.lower() == "packaging")

# When accepting user-entered text you want to compare consistently

category = input("Category: ").strip().lower()
print(category == "packaging")
```

#### guided_lessons/conditionals.py

```python
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
```

#### guided_lessons/combine_conditionals.py

```python
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
```

#### guided_lessons/worked_example.py

```python
available_rolls = 12
requested_rolls = int(input("Rolls to reserve: "))

if requested_rolls < 0:
    print("Requested value cannot be negative.")
elif requested_rolls == 0:
    print("Nothing was reserved")
elif requested_rolls > available_rolls:
    print("Not enough rolls to fill request. ")
else: 
    available_rolls = available_rolls - requested_rolls
    print(f"Requested rolls: {requested_rolls}")
    print(f"Remaining rolls: {available_rolls}")

print("Reservation check complete.")
```

### Independant practice

#### independant_practice/predict_output.py

```python

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
```

#### independant_practice/predict_outputs_2.py

```python
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
```

#### independant_practice/repair_decision_order.py

```python
# The program runs, but zero stock receives the wrong status. 
#
# 1. Explain why it prints the wrong status
# 2. Fix the ordering so zero prints OUT OF STOCK
# 3. Rerun corrected program with 0, 10, and 11
# 4. Include each result


# remaining_rolls = 0

# if remaining_rolls <= 10:
#     print("LOW STOCK")
# elif remaining_rolls == 0:
#     print("OUT OF STOCK")
# else:
#     print("STOCK OK")

remaining_rolls = 11

if remaining_rolls == 0:
    print("OUT OF STOCK")
elif remaining_rolls <= 10:
    print("LOW STOCK")
else: print("STOCK OK")

#1. the remaining rolls at the beginning checked if the rolls were less than or equal to 10 which is True but ends the chain. The check for 0 must occur first
#2. Order is fixed in above code
#3. Reran
#4. Results 0: OUT OF STOCK , 10: LOW STOCK, 11: STOCK OK
```

#### independant_practice/inventory_decision.py

```python
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

```

#### independant_practice/stretch.py

```python
# Check a prompt before submission

# Ask user to enter a prompt, strips white space and converts to lower case
prompt = input("Enter your prompt here...").strip().lower()
# Checks length of the prompt
prompt_length = len(prompt)

# Boolean flags
empty_prompt = False
short_prompt = False
long_prompt = False

# Conditionals
if prompt_length == 0:
    empty_prompt = True

if prompt_length < 10:
    short_prompt = True

if prompt_length > 200:
    long_prompt = True

if empty_prompt:
    print("You have supplied no prompt")
elif short_prompt:
    print("You have supplied too short of a prompt")
elif long_prompt:
    print("You have supplied too long of a prompt")
else:
    print("Your prompt was accepted.")
```

