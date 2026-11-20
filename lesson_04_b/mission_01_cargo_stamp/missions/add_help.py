tokens = 2
activations = 0

while True:
    command = input("Rune machine [activate/inspect/leave/help]: ").strip().lower()

    if command == "inspect":
        print(f"Tokens: {tokens}; activations: {activations}")
        continue
    elif command == "help":
        print("Available commands are:\n1.Activate\n2.Inspect\n3.Leave\n4.Help")
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

# What would happen if you remove continue from the inspection branch?

# Removing continue would end the branch and print that the cargo lift rises.

# Why is break appropriate for leave?

# Break exits the program. We want to finish when we leave

# Which statement changes the stored state?

# tokens -= 1 and activations += 1