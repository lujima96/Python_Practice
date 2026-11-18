# A loop repeats a block of instructions. Each trip through the block is an iteration.
for tower in range(1,4):
    print(f"Tower {tower}: beacon lit")

print("Patrol complete.")

# Range boundaries

# range(4) supplies values 0,1,2,3
# range(1,4) supplies values 1,2,3
# range(2,7) supplies values 2,3,4,5,6
# range(3,0,-1) supplies values 3,2,1

# Forms
# range(stop): start at zero
# range(start,stop): choose starting value
# range(start,stop,step): Changes increment amount

# Stop value is EXCLUDED
# A common off-by-one error happens when your b oundary causes one too many or one too few iterations.