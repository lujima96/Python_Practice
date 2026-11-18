# The program runs, but zero stock receives the wrong status. 
#
# 1. Explain why it prints the wrong status
# 2. Fix the ordering so zero prints OUT OF STOCK
# 3. Rerun corrected program with 0, 10, and 11
# 4. Include each result


# remaining_rolls = 0

# if remaining_rolls <= 10:
#     print("LOW STOCK")
# elif remaining_rolls == 0:
#     print("OUT OF STOCK")
# else:
#     print("STOCK OK")

remaining_rolls = 11

if remaining_rolls == 0:
    print("OUT OF STOCK")
elif remaining_rolls <= 10:
    print("LOW STOCK")
else: print("STOCK OK")

#1. the remaining rolls at the beginning checked if the rolls were less than or equal to 10 which is True but ends the chain. The check for 0 must occur first
#2. Order is fixed in above code
#3. Reran
#4. Results 0: OUT OF STOCK , 10: LOW STOCK, 11: STOCK OK