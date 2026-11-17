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