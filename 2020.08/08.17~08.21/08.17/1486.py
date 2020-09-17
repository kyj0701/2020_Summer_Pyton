# start = 0, n = 5

nums = []

for i in range(n):
    nums.append(start + 2 * i)
    
for i in range(n):
    if i < n - 1:
        nums[i+1] = nums[i] ^ nums[i+1]
    else:
        return nums[i]