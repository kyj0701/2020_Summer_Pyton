import operator

nums = [1,1,1,2,2,3]
k = 2

el = set(nums)
fre = {}


for i in nums:
    if i in fre:
        fre[i] += 1
    else:
        fre[i] = 1

print(fre)
    
res = sorted(fre.items(), key = operator.itemgetter(1), reverse = True)

print(sorted([res[i][0] for i in range(k)]))