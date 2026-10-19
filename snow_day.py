# Independent check: Snow day
# Work alone: no AI, no notes. Write your prediction on paper BEFORE you run anything.
#
# 1. Predict: write the exact output of this program on paper.
# 2. Debug:   make school_status follow the rule in the comment inside it.
# 3. Adjust:  the district also closes school when there are more than 4 inches
#             of snow and it is below freezing. Change the closed condition so it
#             uses one `or` and one `and`, with no parentheses. Then explain why
#             Python gets the right answer without parentheses.
# 4. Test:    change Wednesday's call to school_status(4, True). Predict the
#             output on paper, then run it.

def school_status(snow_inches, below_freezing):
    # more than 8 inches: closed. More than 2 inches: delayed. Otherwise: open.
    if snow_inches > 2:
        return "Delayed opening"
    if snow_inches > 8:
        return "School closed"
    return "Open as usual"

print("Monday:", school_status(10, False))
print("Tuesday:", school_status(5, True))
print("Wednesday:", school_status(1, True))

# 1. Prediction:
#
# Actual:
#
# Because (name a big idea number):
#
# 3. Why no parentheses are needed:
#
# 4. Test prediction (Wednesday, 4 inches):
#
# Actual:
