# nums = [3,2,3]
# nums = [1,1,1,3,3,2,2,2]

cnt = {}
res = []

for i in nums:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1
        
    if cnt[i] > len(nums)//3 and not i in res:
        res.append(i)
        
print(res)