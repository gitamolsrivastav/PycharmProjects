# def string_compress(x):
#     # d = {}
#     # for i in x:
#     #     if i not in d:
#     #         d[i] = 1
#     #     else:
#     #         d[i] += 1
#     # print(d.items())
#     # print("".join(['%s%s' %(k, v) for k, v in d.items()]))
#     r = " "
#     l = len(x)
#     if l == 1:
#         return str(x)+"1"
#     if l == 0:
#         return "NONE"
#     curr = x[0]
#     counter = 1
#     i= 1
#     while i < l:
#         if x[i-1] == x[i]:
#             counter = counter + 1
#         else:
#             r = r + x[i-1] + str(counter)
#             counter = 1
#         i = i + 1
#     r = r + x[i - 1] + str(counter)
#     return r
#
# print(string_compress('AAABCBCBC'))


# def pali(x):
#     l = len(x)
#     high = l - 1
#     low = 0
#     while(low < high):
#         if x[low] != x[high]:
#             return False
#         else:
#             low += 1
#             high -= 1
#     return True
#
# print(pali("badaba"))

def merge_sort(arr):
    if len(arr) > 1:

        mid = len(arr)//2

        leftA = arr[: mid]
        rightA = arr[mid :]

        merge_sort(leftA)
        merge_sort(rightA)

        i, j, k = 0, 0, 0

        while i < len(leftA)  and j < len(rightA):
            if leftA[i] < rightA[j]:
                arr[k]= leftA[i]
                i +=1
            else:
                arr[k] = rightA[j]
                j +=1
            k += 1
        while i < len(leftA):
            arr[k] = leftA[i]
            i += 1
            k += 1
        while j < len(rightA):
            arr[k] = rightA[j]
            j += 1
            k += 1
    return arr

arr = [11, 2, 5, 4, 7, 56, 2, 12, 23]

print(merge_sort(arr))











