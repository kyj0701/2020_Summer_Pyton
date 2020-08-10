ans = []

while nums:
    for i in range(nums[0]):
        ans.append(nums[1])
    nums.pop(0)
    nums.pop(0)

print(ans)