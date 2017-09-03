# def dup(arr):
#     size = len(arr)
#     hs = set()
#     i = 0
#     while i < size:
#         if arr[i] in hs:
#             print(arr[i])
#         else:
#             hs.add(arr[i])
#         i += 1
#
#     return hs
#
# print(dup([1,2,3,4,2,4,9]))
################################
# def miss(arr):
#     i = 0
#     missL = []
#     listj = range(1,7)
#     size = len(listj)
#     while i < size:
#         if listj[i] in arr:
#             i += 1
#         else:
#             missL.append(listj[i])
#             i += 1
#     return missL
#
#
# print(miss([1,2,5,6]))
# def finder(arr1, arr2):
#     arr1.sort()
#     arr2.sort()
#
#     for num1, num2 in zip(arr1, arr2):
#         #print(zip(arr1, arr2))
#         if num1 != num2:
#             return num1
#
#     #return num1
#
# print(finder([1,2,3,4,5,6,7], [3,7,2,1,5,6]))
import collections
def finder2(arr1, arr2):
    d = collections.defaultdict(int)

    for num in arr2:
        d[num] = d[num] + 1

    for num in arr1:
        if d[num] == 0:
            return num

        else:
            d[num] -= 1




print(finder2([1,2,3,4,5,6,7], [3,7,2,1,5,6]))




