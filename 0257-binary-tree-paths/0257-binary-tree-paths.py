# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node, path, arr):
            if not node:
                return 
            path += str(node.val)
            if not node.right and not node.left:
                arr.append(path)
            else:
                dfs(node.left, path+'->',arr)
                dfs(node.right,path+'->',arr)
            
        arr = []
        dfs(root, '', arr)
        return arr