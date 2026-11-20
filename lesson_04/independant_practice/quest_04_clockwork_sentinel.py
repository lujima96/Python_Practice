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

