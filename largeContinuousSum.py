def largeSum(arr):
    if len(arr) == 0:
        return 0
    max_sum1 = curr_sum = arr[0]
    for num in arr[1:]:
        curr_sum = max(curr_sum+num, num)
        # if curr_sum + num > num:
        #     curr_sum = curr_sum + num
        # else:
        #     curr_sum = num

        #if curr_sum < max_sum1:
        max_sum1 = max(max_sum1,curr_sum)
    return max_sum1

arr = [1, 2, -1, 3, 4, 10, 10, -10, -1]
print(largeSum(arr))




