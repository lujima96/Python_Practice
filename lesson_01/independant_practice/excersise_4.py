#identify bug and fix

item_name = "Label roll"
rolls_available = 32

print("Item:", item_name)
#capital r causes the print statement to reference a variable that does not exist. The fix is to use 'rolls_available'
print("Rolls available:", rolls_available)