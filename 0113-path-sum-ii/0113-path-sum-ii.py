# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def find(root, targetSum, path):
            if not root:
                return
            new = path + [root.val]

            if not root.left and not root.right and targetSum == root.val:
                ans.append(new)
            else:
                find(root.left, targetSum - root.val, new)
                find(root.right, targetSum - root.val, new)
            
        ans = []
        find(root,targetSum, [])
        return ans