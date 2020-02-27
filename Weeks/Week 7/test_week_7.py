# def my_function(fname, lname):
#     print("Hello " + fname,lname)
#     return "x"
#
# print(my_function("A","B"))

# def my_numbers(x,y):
#     a = x + y
#     return a
#
# print(my_numbers(4,5))


# def my_max(n1,n2,n3,n4):
#     max1 = max(n1,n2,n3,n4)
#     return max1
#
# print(my_max(10,50,50,100))

# def print_name(fname,lname =""):
#     print(fname + " " + lname)
#
# print_name('A')


# def isnumneg(n):
#     if n < 0:
#         return True
#     return False

def isnumneg(n):
    return n < 0


my_value = 2

if isnumneg(my_value):
    print("Number is negative")
else:
    print("Number is positive")


# def divisibleby3(n):
#     return n % 3 == 0
#
# my_number = int(input("What is your number"))
#
# if divisibleby3(my_number):
#     print("Divisible")
# else:
#     print("not")


def list1(my_list, title=""):
    if len(title) > 0:
        print("Title " + title)

    for a in my_list:
        print(a)


colour_list = ["red", "green", "blue", "red"]

list1(colour_list)


def addnumbers(n1: int, n2: int):
    return n1 + n2

addnumbers(3, 3)
