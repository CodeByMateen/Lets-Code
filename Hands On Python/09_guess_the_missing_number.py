# nums = [1, 2, 4, 5, 6]

# method 2
# size = int(input("Enter the size of list: "))
# element_to_skip = int(input("Enter element to skip: "))
# nums = [i for i in range(1, size+1)]
# nums.remove(element_to_skip)

# method 3
# size = int(input("Enter the size of list: "))
# element_to_skip = int(input("Enter element to skip: "))

# nums = [i for i in range(1, size+1) if i != element_to_skip]


# method 4
import random

nums = [1, 2, 3, 4, 5, 6]
nums.remove(3)
random.shuffle(nums)

# since its unsorted and if we don't know the last number
last_num = max(nums)
# last_num = size

# to calculate sum of all numbers from 1 to last number
# math formula

expected_sum = last_num * (last_num+1) // 2
actual_sum = sum(nums)
missing_num = expected_sum - actual_sum
print(missing_num)
