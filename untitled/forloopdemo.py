my_string = 'abcabc'
for c in my_string:
    if c == 'a':
        print('A', end="\t")
    else:
        print(c, end="\t")
print("*"*20)

dicts = {"one": 1, "two": 2, "three": 3}
for d in dicts:
    print(str(dicts[d]))
    print("*"*20)


for k, v in dicts.items():
    print(str(k)+" "+str(v))


l1 = [1, 2, 3, 4]
l2 = [5, 6, 6, 7]
l3 = [10, 20, 30, 40]

for a, b, c in zip(l1, l2, l3):
    print(a)
    print(b)




