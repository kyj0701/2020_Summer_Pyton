num = int("1111011110000011100000110001011011110010111001010111110001", 2)
cnt = 0

while num > 1:
    if num % 2 == 0:
        num = num // 2
        cnt += 1
    else:
        num += 1
        cnt += 1

print(cnt)