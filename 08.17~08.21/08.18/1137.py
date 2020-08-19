# n = 5

t_0 = 0
t_1 = 1
t_2 = 1

if n == 0:
    res = 0
else:
    res = 1

for i in range(n-2):
    res = t_0 + t_1 + t_2
    t_0 = t_1
    t_1 = t_2
    t_2 = res

print(res)