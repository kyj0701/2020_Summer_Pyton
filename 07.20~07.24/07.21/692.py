["i", "love", "leetcode", "i", "love", "coding"]
k = 2

fre = {}

for i in words:
    if i in fre:
        fre[i] += 1
    else:
        fre[i] = 1

print(fre)

res = sorted(fre.items(), key = lambda x:(-x[1],x[0]))


print([res[i][0] for i in range(k)])