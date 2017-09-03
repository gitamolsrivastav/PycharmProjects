def getMax(arr):
    size = len(arr)
    maxVal = arr[0]
    maxCount = 1
    count = 1
    i = 0
    while i < size:
        j = i + 1
        count = 1
        while j < size:
            if arr[i] == arr[j]:
                count += 1
            j += 1
        if count > maxCount:
            maxCount = count
            maxVal = arr[i]
        i += 1
    return maxVal, maxCount


print(getMax([2,1,1,2,2,4,1,9]))




