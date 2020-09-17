s = input()

re_s = ''
st1 = []
ins = ''
res = ''

for i in s:
    if i.isdigit():
        re_s += i
    
    elif i == '[':
        st1.append(re_s)
        st1.append(i)
        re_s = ''
        
    elif i == ']':
        ins = ''
        while st1[-1] != '[':
            ins = st1.pop() + ins
        st1.pop()
        st1.append(ins * int(st1.pop()))
    
    else:
        st1.append(i)

print(res.join(st1))