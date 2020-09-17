# num = 9669

def maximum69Number (num: int) -> int:
    ins = list(str(num))
    print(ins)
    for i in range(len(ins)):
        if ins[i] == '6':
            ins[i] = '9'
            print(ins)
            return int("".join(ins))
    return num