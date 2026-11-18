# A counter tracks how many times something happens. 
# An accumulator combines values over several iterations, such as a running total

rooms_checked = 0
total_gold = 0

for room in range(1,4):
    rooms_checked += 1
    gold_found = room * 2
    total_gold += gold_found
    print(f"Room {room}: found {gold_found} gold")

print(f"Rooms checked: {rooms_checked}")
print(f"Total gold: {total_gold}")

# Continue skips the rest of this iteration

for room in range(1,5):
    if room == 2:
        print("Room 2 is cursed. Moving on.")
        continue

    print(f"Room {room} is safe to enter")

print("Hallway cleared.")