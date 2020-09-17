import re

s = input()
p = input()

i = re.compile(p)
j = i.match(s)

print(j)