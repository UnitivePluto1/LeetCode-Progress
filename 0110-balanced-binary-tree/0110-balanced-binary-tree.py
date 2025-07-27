# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return [True,0]
            
            leftB, leftH = dfs(root.left)
            rightB, rightH = dfs(root.right)

            isB = leftB and rightB and abs(leftH - rightH) <= 1

            return [isB, 1+max(leftH, rightH)]
        return dfs(root)[0]