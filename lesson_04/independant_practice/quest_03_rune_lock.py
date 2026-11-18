# Mission Rune Lock

# vars
failed_attempts = 0

# Repeatedly ask for a rune or the command leave
while True:
    selection = input("Present a rune or leave!").strip().lower() # Strip surrounding white space and standardize capitalization for mixed inputs
    if selection == "ember":
        print(f"You have opened the gate with {selection}")
        break
    elif selection == "leave":
        print(f"You show great cowardice and retreat.")
        break
    else:
        failed_attempts += 1
        print(f"You have failed {failed_attempts} number of times. Get good.")