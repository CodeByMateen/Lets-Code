nums = [2, 1, 5, 1, 3, 2]
k = 3

current = 0
for i in range(k):
    current += nums[i]

max = current

for i in range(1, len(nums)-k):
    current = current - nums[i-1] + nums[i + k -1]
    if current > max:
        max = current
        
print(max)
