# Repeatedly ask for a rune or the command leave
# Strip surrounding whitespace and accept mixed capitalization
# If the response is ember, print a gate-opening message and end the loop.
# If it is leave, print a retreat message and end the loop.
# Any other response counts as one failed attempt; display a rejection and ask again.
# Print the failed-attempt count after the loop.

# Vars
attempts = 0

while True:
    command = input("Provide a rune or leave: ").strip().lower()
    

    if command == "ember":
        print(f"You open the gate with {command}")
        break
    elif command == "leave":
        print(f"You fail to open the gate and leave")
        break
    else:
        attempts += 1
        print(f"You have failed to open the gate.\nAttempts: {attempts}")

print(f"Total attempts: {attempts}")