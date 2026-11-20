# While loop continues until the condition is satisfied
energy = 3

while energy > 0:
    print(f"Relay pulses. Energy before pulse: {energy}")
    energy -= 1

print(f"Relay stopped. Energy: {energy}")

# Break leaves the loop

while True:
    command = input("Camp command [rest/leave]: ").strip().lower()

    if command == "leave":
        print("You leave camp.")
        break
    elif command == "rest":
        print("You rest by the fire.")
    else:
        print("Unknown command.")

print("Camp closed.")