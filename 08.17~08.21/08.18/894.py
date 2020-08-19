class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    res = dict()
    res[1] = [TreeNode(0)]
    
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if not N in Solution.res:
            ins = []
            for i in range(N):
                j = N - i - 1
                for left in self.allPossibleFBT(i):
                    for right in self.allPossibleFBT(j):
                        t = TreeNode(0)
                        t.left = left
                        t.right = right
                        ins.append(t)
            Solution.res[N] = ins
        return Solution.res[N]