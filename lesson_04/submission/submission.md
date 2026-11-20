### Guided Lessons

#### guided_lesson/for_loops.py

```python
# Repeat a block with for
# Starts at 1, increments to 4 exclusive
for tower in range(1,4):
    print(f"Tower {tower} beacon has been lit.")
print("Patrol complete.")

```

#### guided_lesson/while_loops.py

```python
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
```

#### guided_lesson/counter.py

```python
rooms_checked = 0
total_gold = 0

for room in range (1,4):
    rooms_checked += 1
    gold_found = room * 2
    total_gold += gold_found
    print(f"Room {room}: found {gold_found} gold.")

print(f"Rooms checked: {rooms_checked}")
print(f"Total gold: {total_gold}")
```

#### guided_lesson/continue.py

```python
for room in range(1,5):
    if room == 2:
        print("Room 2 is cursed. Moving on.")
        continue

    print(f"Room {room}: safe to enter.")

print("Hallway cleared.")
```

### Independant practice

#### independant_practice/quest_01_watchtower_patrol.py

```python
for tower in range(1,7):
    print(f"Tower {tower} beacon has been lit.")

print("All six beacons are lit.")

# Why did you choose your stop?

# Second value in range is exlusive so 6 would not be included at a stop value of 6

# What would change if you used range(1,6)?

# 5 would be the last beacon lit printed
```

#### independant_practice/quest_02_cursed_halls.py

```python
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
```

#### independant_practice/quest_03_open_the_rune_lock.py

```python
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
```

#### independant_practice/quest_04_clockwork_sentinel.py

```python
# Starting state
hero_hp = 12
sentinel_hp = 16
potions = 1
turns_taken = 0


# Game loop
while True:
    #accepts commands, strips white space, converts lower case
    command = input(
        "Choose your action\n1. Attack\n2. Heal\n3. Status\n4. Flee\nYour choice: "
        ).strip().lower()

    if command == "1" or command == "attack":
        sentinel_hp -= 4
        print("You strike the sentinel for 4 damage")

    elif command == "2" or command == "heal":
        if potions == 0:
            print("You are out of potions")
            continue

        potions -= 1
        hero_hp = 12
        print("Your health has been restored to 12.")

    elif command == "3" or command == "statis":
        print(f"Hero HP {hero_hp}")
        print(f"Sentinel HP: {sentinel_hp}")
        print(f"Potions: {potions}")
        print(f"Turns: {turns_taken}")
        continue

    turns_taken += 1

    if sentinel_hp <= 0:
        sentinel_hp = 0
        outcome = "Victory"
        break

    hero_hp -= 5

    if hero_hp < 0:
        hero_hp = 0

    print(f"The sentinel retaliates. Hero HP: {hero_hp}")

    if hero_hp == 0:
        outcome = "Defeat"
        break

print(f"\n{outcome}")
print(f"Hero HP: {hero_hp}")
print(f"Sentinel HP: {sentinel_hp}")
print(f"Potions: {potions}")
print(f"Turns: {turns_taken}")

```

#### independant_practice/side_quest.py

```python
weight = 0.0
target = 5.0
learning_rate = 1.1

for step in range(1, 9):
    prediction = weight
    error = prediction - target
    loss = error ** 2

    print(f"Step {step}: weight={weight:.3f}, loss={loss:.3f}")

    gradient = 2 * error
    weight = weight - learning_rate * gradient

print(f"Final weight: {weight:.3f}")

# Compare loss values
# Losses are increased at higher learning rates
# Repeating updates:
# Repeated updates amplifies losses
# Loss values are carried forward, weights are recalculated.
```

