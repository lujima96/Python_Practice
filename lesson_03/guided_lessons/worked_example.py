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