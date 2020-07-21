class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        rlist = []
        r = ListNode()
        
        while True:
            if head.next != None:
                rlist.append(head.val)
                head = head.next
            else:
                rlist.append(head.val)
                break
                
        size = len(rlist)
        
        while len(rlist) != 0:
            if len(rlist) == size:
                ins = ListNode(rlist.pop(), None)
                r = ins
            elif len(rlist) > 0:
                ins = ListNode(rlist.pop(), None)
                r.next = ins
                
        return r


Solution.reverseList([1,2,3,4,5])