def searchBST(self, root: TreeNode, val: int) -> TreeNode:
    if not root:
        return None
    if root.val == val:
        return root
    else:
        return self.searchBST(root.left, val) or self.searchBST(root.right, val)