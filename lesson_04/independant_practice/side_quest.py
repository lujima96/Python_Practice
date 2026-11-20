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