# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxi):
            if not node:
                return 0
            
            good = 1 if node.val >= maxi else 0 

            maxi = max(node.val, maxi)
            
            good += dfs(node.right, maxi)
            good += dfs(node.left, maxi)

            return good


        return dfs(root, root.val)