limit = 4

# Draw a box (method #1)

for a in range(int(limit)):

    for b in range(int(limit)):
        print("*", end="")

    print()

for a in range(limit):
    print("#" * limit)

# Draw a right-sided triangle

for a in range(limit):
    print("$" * (a+1))