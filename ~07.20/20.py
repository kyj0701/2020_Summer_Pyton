s = input()

a = []
c = 0
        
for i in s:
	if i == '(' or i == '{' or i == '[':
		a.append(i)
		c += 1
	elif i == ')':
		if a != [] and a.pop() == '(':
			c -= 1
			continue
		else:
			print(False)
	elif i == '}':
		if a != [] and a.pop() == '{':
			c -= 1
			continue
		else:
			print(False)
	elif i == ']':
		if a != [] and a.pop() == '[':
			c -= 1
			continue
		else:
			print(False)
		

if a == [] and c ==0:
	print(True)
