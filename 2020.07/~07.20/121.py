import sys

prices = [7,6,4,3,1]


price = sys.maxsize
profit = 0
print(price)


for i in prices:
    if i < price:
        price = i
        print(price)
    else:
        if i - price > profit:
            profit = i - price
    # print(price)
    # print(profit)

print(profit)