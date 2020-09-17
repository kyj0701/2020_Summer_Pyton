# s = 'RLRRLLRLRL'

sp = list(s)
stack = []
cnt = 0
    
while sp:
    if not stack or sp[0] == stack[-1]:
        stack.append(sp[0])
        sp.pop(0)
    else:
        stack.pop()
        sp.pop(0)
    if not stack:
        cnt += 1
    
print(cnt)