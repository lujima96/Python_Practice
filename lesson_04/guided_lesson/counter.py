rooms_checked = 0
total_gold = 0

for room in range (1,4):
    rooms_checked += 1
    gold_found = room * 2
    total_gold += gold_found
    print(f"Room {room}: found {gold_found} gold.")

print(f"Rooms checked: {rooms_checked}")
print(f"Total gold: {total_gold}")