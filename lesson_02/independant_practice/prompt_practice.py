# Write a program that asks for a topic and a target audience, then prints:
# Explain networking to restaurant managers using a practical example.
# Optionally add a character count
topic = str(input("Enter your chosen topic: "))
target_audience = str(input("Enter your target audience: "))

prompt = f"Explain {topic} to {target_audience} using a practical example."
character_count = len(prompt)

print(f"{prompt}\nCharacter count: {character_count}")