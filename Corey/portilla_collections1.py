# from collections import Counter
from functools import reduce
#
# l = [1,1,1,11,1,1,1,1,2,2,2,2,4,4,45,5,5,5,5]
#
# s = 'fdsfsfsdfdffgggg'
#
# _s = Counter(s)
#
# print(Counter(l))
#
# print(_s)
#
# print(Counter(s).most_common(10))
#
# print(sum(_s.values()))

# tuple of dictionary

def frhttocelcius(val):

    while True:

        try:
            #val = int(input("Enter the operand: "))
            c = 5.0/9.0 * (val-32)
        except Exception as e:
            print("ERROR MESSAGE: ", e)
            print("Try again with valid value!")
            continue
        else:
            return c


        finally:
            print("EXECUTE")
temp = [30, 50, 60, 80]
temp_list = list(map(lambda v:  v*100, temp))
print(temp_list)
print(frhttocelcius(32))

max_find = lambda a,b: a if a>b else b

print(reduce(max_find,temp))

def strrev(x):
    x_list = x.split(" ")
    res = []

    print(x_list)
    count = len(x_list)
    i =0

    for val in x_list:
        if count >i:

            i =+ 1

    print(res)

strrev("I am vivek")

def reverse(text):
    rev = ''
    for i in range(len(text), 0, -1):
        rev += text[i-1]
    print(rev)

reverse("I am Vivek")


