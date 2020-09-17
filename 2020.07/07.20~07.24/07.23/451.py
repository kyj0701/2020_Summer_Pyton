# s = "tree"
# s = "cccaaa"
# s = "Aabb"

cnt = {}
res = ""

for i in s:
    if not i in cnt:
        cnt[i] = 1
    else:
        cnt[i] += 1

ins = sorted(cnt.items(), key = lambda x:x[1], reverse = True)

for i in ins:
    res += (i[0] * i[1])
    
print(res)