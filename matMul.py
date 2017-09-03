def index(lst):


    output = [1] * len(lst)
    product = 1
    i = 0

    while i < len(lst):
        output[i] = product
        product = product * lst[i]
        i = i + 1
    product = 1
    i = len(lst) - 1
    while i >= 0:
        output[i] *= product
        product *= lst[i]
        i -= 1
    return output

lst = [3, 2, 4, 1, 5]
print(index(lst))

#brute force technique
print("*"*200)
def a_index():
    arr = [3, 2, 4, 1, 5]

    size = len(arr)
    out = [1] * size
    prod = 1
    i=0
    for num in arr:
        prod = prod * num
    print(prod)
    while i < size:
        out[i] = prod//arr[i]
        i += 1
    return out


print(a_index())



