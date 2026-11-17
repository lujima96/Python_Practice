# Assigns '  PACKAGING  ' to category
category = "  PACKAGING  "

# Strips the white space to the left and right turning category to 'Packaging'
category.strip()

# f string printing 'Category: [PACKAGING]
## Error was made in this prediction. The stripped 'PACKAGING' was not assigned to the var at this time yet
print(f"Category: [{category}]")

# Performs both a strip and a lower case operation on category
## This is where it is actualy assigned
category = category.strip().lower()

# f string printing 'Category: [packaging]'
print(f"Category: [{category}]")