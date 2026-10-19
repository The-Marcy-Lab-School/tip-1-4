def pack_bag(temp, raining):
    if raining:
        print("umbrella")
    if temp < 50:
        print("gloves")
    if temp > 80:
        print("water bottle")

def pick_coat(temp):
    if temp < 32:
        print("winter coat")
    if temp < 50:
        print("jacket")
    if temp < 65:
        print("hoodie")

print("--- pack_bag(45, True)")
pack_bag(45, True)
# Prediction:
# Actual:
# Explanation:

print("--- pack_bag(70, False)")
pack_bag(70, False)
# Prediction:
# Actual:
# Explanation:

print("--- pick_coat(20)")
pick_coat(20)
# Prediction:
# Actual:
# Explanation:

print("--- pick_coat(40)")
pick_coat(40)
# Prediction:
# Actual:
# Explanation:
