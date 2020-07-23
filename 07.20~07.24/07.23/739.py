# T = [73, 74, 75, 71, 69, 72, 76, 73]

st = []
res = [0] * len(T)

for i in range(0,len(T)):
    while st and T[i] > T[st[-1]]:
        index = st.pop()
        res[index] = i-index
    st.append(i)

print(res)