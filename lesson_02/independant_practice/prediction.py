# Predict the output 

# boxes assigned string value of '6'
boxes = "6"
# rolls_per_box assigned string value of '24'
rolls_per_box = "24"

# Concatenates to 624
print(boxes + rolls_per_box)

#Int conversion for both strings then multiplied together 6 * 24 = 144
print(int(boxes) * int(rolls_per_box))

# Prints value assigned to boxes within an f string. Output 'Boxes: 6'
print(f"Boxes: {boxes}")

# F string not used. Expected output 'Boxes: {boxes}'
print("Boxes: {boxes}")