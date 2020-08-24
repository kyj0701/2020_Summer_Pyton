def getDecimalValue(head: ListNode):
    ins = []
    while head:
        ins.append(str(head.val))
        head = head.next
    
    num = int("".join(ins),2)
    return num