n = input()
n = int(n)

cnt = 0
        
if n == 1 or n == 0:
    print(n)

else:        
    for i in range(1, n):
        if n >= i:
            n = n - i
            cnt += 1
            # print(cnt)
        else:
            break

print(cnt)