# Cleaning strings
item_name = "  Label Roll  "

## White Space Strip
print(item_name.strip())

### Lower Case
print(item_name.lower())

# These methods return new strings but do not automatically change the variable

car_make = "  Toyota  "
car_make.strip()
print("Make:", car_make)

# To keep the results you need to assign it to a variable

car_make = car_make.strip()
print("Make:", car_make)

# You can combine methods for cleaning

car_make = input("Enter your car make:").strip().lower()
print(car_make)

