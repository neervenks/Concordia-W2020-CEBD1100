mylist = [4, 5, 10, 20, 10, 54, 22, 1, 20, 20]

# Requirement 1:
#   Get the lowest value
# Requirement 2:
#   Get the highest value
# Requirement 3:
#   PRint a list of duplicate numbers.

min = mylist[0]
max = mylist[0]

for x in mylist:

    #min
    if x < min:
        min = x

    if x > max:
        max = x

print(min)
print(max)

