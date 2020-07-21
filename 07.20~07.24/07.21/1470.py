nums = [2,5,1,3,4,7]
n = len(nums)/2

res = []
nums1 = nums[0:n]
nums2 = nums[n:len(nums)]

for i in range(n):
    res.append(nums1[i])
    res.append(nums2[i])
    
return res