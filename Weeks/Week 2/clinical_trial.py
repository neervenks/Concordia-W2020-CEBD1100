age = input("Age    > ")
sex = input("M or F > ")
age  = int(age)

if not (age < 20 and sex == "M"):
    print("The candidate is OK")

