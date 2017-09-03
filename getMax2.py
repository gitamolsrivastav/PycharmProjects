def getMax2(arr):
    size = len(arr)
    arr.sort()
    maximum = arr[0]
    maxCount = 1
    curr = arr[0]
    currCount = 1
    arr.sort()

    i = 1
    while i < size:
        if arr[i] == arr[i-1]:
            currCount += 1
        else:
            currCount = 1
            curr = arr[i]
        if currCount > maxCount:
            maxCount = currCount
            maximum = curr
        i = i +1
    return maxCount, maximum


print(getMax2([2,1,2,1,2,4,1,9]))