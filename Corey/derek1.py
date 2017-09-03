name = input("whats your name")

print("hello", name)

num1, num2 = input('Enter 2 number: ').split()

num1 = int(num1)
num2 = int(num2)

sum = num1 + num2

print("{} + {} = {}".format(num1, num2, sum))

num3, operator, num4 = input('Enter calculation: ').split()

num3 = int(num3)
num4 = int(num4)

if operator == "+":
    print("{} + {} = {}".format(num3, num4, num3+num4))
elif operator == "-":
    print("{} - {} = {}".format(num3, num4, num3-num4))
elif operator == "/":
    print("{} / {} = {}".format(num3, num4, num3/num4))
elif operator == "*":
    print("{} * {} = {}".format(num3, num4, num3*num4))
else:
    print("Use valid operators")




