tokens = 2
activations = 0

while True:
    command = input("Rune machine [activate/inspect/leave]: ").strip().lower()

    if command == "inspect":
        print(f"Tokens: {tokens}; activations: {activations}")
        continue
    elif command == "leave":
        break
    elif command != "activate":
        print("Unknown command.")
        continue

    if tokens == 0:
        print("No rune tokens remain.")
        continue

    tokens -= 1
    activations += 1
    print("The cargo lift rises.")

print(f"Machine closed after {activations} activations.")