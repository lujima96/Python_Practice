Setup: My operating system is PopOS!. Python is installed. My editor is VScode.


Code from excersises 

Guided Lessons: 
#String print

print("Inventory Check")
print("Main storeroom")

#Integener print
print(12)

#Operation print
print(12+3)

#concatenation print
print("12"+"3")

# '' or "" can be used for simple print
print("Label Roll")
print('Label Roll')

#Variables
item_name = "Label Roll"
quantity = 12

#Print Vars
print(item_name)
print(quantity)

#Name differs from literal
print("quantity")

#Readable names are important. Lowercase letters, digits, underscores, and starting with a letter is good practice
boxes_received = 4
rolls_per_box = 25

#Python expressions include + (addition), - (subtraction), *(multiplication), / (division), ** (exponent), % (modulo or remainder)

#Expressions can use variables
rolls_received = boxes_received * rolls_per_box
print(rolls_received)

# () can be used to control grouping for mathematical operations, remember PEMDAS
print(2 + 3 * 4)
print((2 + 3) * 4)

# Printing results with context can help the end user understand better what is provided
print("Rolls received:", rolls_received)

# Assignment 
papers_printed = 2
words_per_page = 500

#calculates based on provided variables
total_words = papers_printed * words_per_page
print("Words printed:", total_words)

#variable updates but has not been recalculated
papers_printed = 30

#recalculate with new vars
total_words = papers_printed * words_per_page

print("Words printed:", total_words)

#variables can use their own previous values

papers_printed = 5000
papers_printed = papers_printed - 490
print(papers_printed)

Independant practice

1. 
# Predict and explain

#Integer 8 assigned to quantity
quantity = 8
#Total = 8 * 3 (24)
total = quantity * 3
#quantity reassigned 
quantity = 10

#predicted print value of 10
print(quantity)
#predicted total value of 24
print(total)

#ACTUAL OUTPUT
#10
#24

2. 
# Build inventory calculator
# Step 1 define boxes, rolls_per_box, and rolls_used

boxes = 100
rolls_per_box = 25
rolls_used = 40

# Step 2 calculate starting rolls

starting_rolls = boxes * rolls_per_box

# Step 3 calculate remaining rolls

remaining_rolls = starting_rolls - rolls_used

# Step 4 print with context
print("Starting rolls:",starting_rolls)
print("Remaining rolls:",remaining_rolls)

# Step 5 2 new boxes arrive

boxes_delivered = 2

#add new boxes to the total
boxes += boxes_delivered

rolls_delivered = boxes_delivered * rolls_per_box

remaining_rolls += (boxes_delivered * rolls_per_box)
print("Remaining rolls:",remaining_rolls)

3. 
remaining_rolls = 2000
# Text or var?

# Prints the value assigned to remaining rolls 
print(remaining_rolls)

# Prints the string literal "remaining_rolls"
print("remaining_rolls")
4. 
#identify bug and fix

item_name = "Label roll"
rolls_available = 32

print("Item:", item_name)
#capital r causes the print statement to reference a variable that does not exist. The fix is to use 'rolls_available'
print("Rolls available:", Rolls_available)