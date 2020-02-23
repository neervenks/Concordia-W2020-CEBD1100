# The following file prints lines 0 through 30.
# In each line we follow the following logic:
# A) If the line number is divisible by 3, print "Fizz".
# B) If the line number is divisible by 5, print "Buzz".

for line_numb in range(0, 31):

    print(str(line_numb) + ": ", end="")

    if line_numb % 3 == 0:
        print("Fizz", end="")

    if line_numb % 5 == 0:
        print("Buzz", end="")

    print()
