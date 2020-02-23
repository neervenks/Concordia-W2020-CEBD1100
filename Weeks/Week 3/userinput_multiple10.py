inp = ""

while True:

    inp = input("Please enter a number >")

    if inp.upper() == "Q":
        break

    if int(inp) % 10 == 0:
        print("Number is divisible by 10")
    else:
        print("Number is not divisible by 10")
