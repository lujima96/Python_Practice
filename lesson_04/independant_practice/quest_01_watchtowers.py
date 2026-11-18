# Use a for loop to print one message for each tower numbered 1 through 6, inclusive

#Global increment counter
i = 0
for tower in range(1,7):
    i += 1
    print(f"The beacon at tower {tower} has been lit!")
# Print "All six beacons are online." after the loop completes
print(f"All {i} beacons are online.")
# Explains top value and why

# 7 is used as the stop value because it is not inclusive and the final value is excluded

# Prediction check:
#   What would change if the loop used range(1,6)?

#       Response:
#               Values 1 - 5 would print. The last message would be The beacons at tower 5 have been lit from the loop.