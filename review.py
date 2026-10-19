def is_it_hot(temp):
    if temp > 100:
        print("So Hot!")
    elif temp > 90:
        print("Yes!")
    elif temp > 75:
        print("Eh")
    else:
        print("Nah")

is_it_hot(95)
is_it_hot(60)

# R1
# Temperature I picked:
# Prediction:
# Actual:
# How many lines printed, and why:

# R2
# Why only Yes! and not Eh too:

# R3
# How the conditions go from narrowest to broadest:
# If temp > 75 were first, is_it_hot(95) would print:

# R4
# The else runs for any temperature that is:
# Prediction for is_it_hot(75):
# Actual:
# Prediction for is_it_hot(76):
# Actual:
