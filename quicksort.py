def quick_sort(arr):
        size = len(arr)
        quick_sort_help(arr, 0, size-1)


def quick_sort_help(arr,first,last):

    if first < last:

        splitpoint = partition(arr,first,last)

        quick_sort_help(arr,first, splitpoint-1)
        quick_sort_help(arr, splitpoint+1, last)

def partition(arr,first,last):

    pivotvalue = arr[first]

    leftmark = first + 1
    rightmark = last

    done = False

    while not done:


        while leftmark <= rightmark  and arr[leftmark] < pivotvalue:

            leftmark += 1

        while rightmark >= leftmark  and arr[rightmark] > pivotvalue:

            rightmark -= 1

        if rightmark < leftmark:

            done = True

        else:

            temp = arr[leftmark]
            arr[leftmark] = arr[rightmark]
            arr[rightmark] = temp

    temp = arr[first]
    arr[first] = arr[rightmark]
    arr[rightmark] = temp

    return rightmark



arr = [54, 26, 93, 17]
quick_sort(arr)
print(arr)

