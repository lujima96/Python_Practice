# Vars
rooms_to_visit = int(input("Enter the number of rooms to visit: "))
rooms_visited = 0
gold_acquired = 0
cursed_room_count = 0

# Bools
valid_input = True

for room in range(1, rooms_to_visit + 1):
    # Reject invalid inputs
    if rooms_to_visit > 0:
        valid_input = True
    else:
        valid_input = False
        print("You have entered an invalid input.")

    # Count every inspected room
    rooms_visited += 1
    if room == 3 or room == 6:
        print(f"Room {room} is cursed and provides no loot")
        cursed_room_count += 1
    else:
        gold_acquired += 3
        print(f"You acquired 3 gold from room {room}. Your total is {gold_acquired}")
        continue

# Final Summary
print(f"Total rooms visited during expedition: {rooms_visited}")
print(f"Total gold acquired: {gold_acquired}")
print(f"Cursed rooms: {cursed_room_count}")

# The inspected room count needs to increase first so it is in sync with the room you are in and the rest of the program logic follows.