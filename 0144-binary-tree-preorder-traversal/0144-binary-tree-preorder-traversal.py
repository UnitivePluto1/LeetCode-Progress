# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            temp = stack.pop()
            res.append(temp.val)
            if temp.right:
                stack.append(temp.right)
            if temp.left:
                stack.append(temp.left)
        return res
