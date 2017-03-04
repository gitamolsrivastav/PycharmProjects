def sum_nums(n1, n2):
    return n1 + n2

sum1 = sum_nums(3, 4)
print (sum1)
print("*"*100)

def isMetro(cityname):
    l1 = ['sfo', 'la', 'boston']
    if cityname in l1:
        return True
    else:
        return False

x = isMetro('boston')

print(x)
print("*"*100)

def large_num(*args):
    print(min(*args))


large_num(-20, 30, 100, 89)








