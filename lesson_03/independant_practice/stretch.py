# Check a prompt before submission

# Ask user to enter a prompt, strips white space and converts to lower case
prompt = input("Enter your prompt here...").strip().lower()
# Checks length of the prompt
prompt_length = len(prompt)

# Boolean flags
empty_prompt = False
short_prompt = False
long_prompt = False

# Conditionals
if prompt_length == 0:
    empty_prompt = True

if prompt_length < 10:
    short_prompt = True

if prompt_length > 200:
    long_prompt = True

if empty_prompt:
    print("You have supplied no prompt")
elif short_prompt:
    print("You have supplied too short of a prompt")
elif long_prompt:
    print("You have supplied too long of a prompt")
else:
    print("Your prompt was accepted.")