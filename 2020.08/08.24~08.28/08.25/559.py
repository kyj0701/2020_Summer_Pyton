def maxDepth(self, root: 'Node') -> int:
    if not root:
        return 0
    elif not root.children:
        return 1
    else:
        return 1 + max(map(self.maxDepth, root.children))