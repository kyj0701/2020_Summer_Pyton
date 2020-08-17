#  nums = [1,3,5,6] target = 5

for i in nums:
    if i >= target:
        return nums.index(i)
print(len(nums))