# For loops are useful when you have a sequence of values to process. A while loop repeats WHILE a condition is true

energy = 3

while energy > 0:
    print(f"Relay pulses. Energy before pulse {energy}")
    energy -= 1

# The condition is checked before each iteration, including the first one..

# Break leaves the loop. Sometimes you cannot know how many times someone will enter a command. You can use while True and leave with a breakL

while True:
    command = input("Camp command [rest/leave]: ").strip().lower()

    if command == "leave":
        print("Leaving camp.")
        break
    elif command == "rest":
        print("You rest by the fire.")
    else: 
        print("Unknown command.")

print("Camp closed.")