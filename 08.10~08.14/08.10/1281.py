digits = str(n)
product = 1
sum = 0

for i in digits:
    product = product * int(i)
    sum = sum + int(i)

print(product - sum)