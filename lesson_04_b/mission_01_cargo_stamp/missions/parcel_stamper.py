parcel_count = int(input("Enter a number of parcels to be stamped: "))

if parcel_count > 4 or parcel_count < 0:
    print("Invalid input.")

elif parcel_count == 0:
    print("You provided no parcels to count")

elif parcel_count >= 1 or parcel_count <= 4:
    for parcel in range(1, parcel_count +1):
        print(f"Parcel {parcel} has been stamped")




    
if parcel_count in range(0,4 +1):   
    print(f"{parcel_count} parcels have been stamped")

# Who should the count check happen before the loop?

# You need to make sure your count is valid before you move any further in the program

