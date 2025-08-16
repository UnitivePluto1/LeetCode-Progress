# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [(root, root.val)]
        good = 0
        while stack:
            curr, maxi = stack.pop()
            if curr.val >= maxi:
                good+=1
            maxi = max(maxi, curr.val)
            if curr.right:
                stack.append((curr.right, maxi))
            if curr.left:
                stack.append((curr.left, maxi))
        return good