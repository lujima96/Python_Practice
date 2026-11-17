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