dispatch_count = 2

if dispatch_count < 0:
    print("Dispatch count can not be negative.")
else:
    for dispatch in range(1,dispatch_count +1):
        print(f"Dispatch {dispatch}: seal applied")

    print(f"Dispatch desk closed.")