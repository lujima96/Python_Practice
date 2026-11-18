# Input
room_count = int(input("Provide a room count: "))

# Flags
valid_room_count = True

# Vars
gold_count = 0
inspected_rooms = 0

# Conditionals
if room_count >= 0:
    valid_room_count = True
    print(f"Your number of rooms [{room_count}] is valid.")
else:
    valid_room_count = False
    print(f"Your number of rooms [{room_count}] is invalid")

# inspect rooms numbered 1 through the entered count, inclusive
for room in range(room_count):
    inspected_rooms += 1
    if room == 3 or room == 6:
        print(f"Room {room} is cursed there is no loot to be found")
        continue
    else:
        gold_count += 3

#Summary
if valid_room_count:
    print(f"Total gold is {gold_count} after the expedition.")

#Question: Should the inspected-room counter increase before or after the cursed-room continue?

#Reponse: It needs to happen before otherwise you would be out of sync with which room you are visiting because it would increment afterwards.