inp = ""
mylist = []

while True:

    inp = input("Please enter a number >")

    if inp.upper() == "Q":
        break

    mylist.append(int(inp))

sum = 0
for a in mylist:
    sum += a

print(sum / len(mylist))
