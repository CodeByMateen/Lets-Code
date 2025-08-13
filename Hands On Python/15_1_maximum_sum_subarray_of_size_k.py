'''
Problem 15: Maximum Sum Subarray of Size K
Problem:
Tumhe ek integer array aur ek number k diya hai. Tumhe aise k consecutive elements ka maximum sum find karna hai.

Input: nums = [2, 1, 5, 1, 3, 2], k = 3  
Output: 9  
Explanation: Maximum sum of any 3 consecutive elements is 5 + 1 + 3 = 9
'''

###
'''using sliding window technique'''
###

## solution 1 - by me

nums = [2, 1, 5, 1, 3, 2]
k = 3

current = 0
for i in range(k):
    current += nums[i]

max_sum = current

for i in range(1, len(nums) - k + 1):  # +1 important hai
    current = current - nums[i - 1] + nums[i + k - 1]
    if current > max_sum:
        max_sum = current

print(max_sum)  # Output: 9

## solution 2 by chatgpt

def max_sum_subarray(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum

nums = [2, 1, 5, 1, 3, 2]
k = 3
print(max_sum_subarray(nums, k))

## solution 3 - using random numbers

import random

def maxWindow(arr, k):
    window = sum(arr[:k])
    max_window = window
    for i in range(1, len(arr) - k + 1):
        window = window - arr[i - 1] + arr[i + k - 1]
        max_window = max(max_window, window)
    return max_window

l = [random.randint(0, 9) for _ in range(10)]
k = 4

print(l)
print(maxWindow(l, k))
