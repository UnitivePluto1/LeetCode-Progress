# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        stack = []
        curr = root
        lastv = None

        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                peek = stack[-1]
                if peek.right and lastv != peek.right:
                    curr = peek.right
                else:
                    res.append(peek.val)
                    lastv = stack.pop()
        return res

