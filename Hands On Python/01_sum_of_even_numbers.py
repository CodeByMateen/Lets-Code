def evenSum(nums):
    total = 0
    for i in nums:
        if i%2 == 0:
            total +=i
    return total

nums = [1, 4, 5, 6, 9, 10]
print(evenSum(nums))

# sol 2 using filter and lambda

even_nums = filter(lambda x: x % 2 == 0, nums)
print(sum(even_nums))

# sol 3 using list comprehension

print(sum([x for x in nums if x % 2 == 0]))
