# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        stack1 = [root]
        stack2 = [root]

        while stack1 and stack2:
            curr1 = stack1.pop()
            curr2 = stack2.pop()
            if not curr1 or not curr2:
                return False
            if curr1.val != curr2.val:
                return False
            
            if (curr1.left and not curr2.right) or (not curr1.left and curr2.right):
                return False
            if (curr1.right and not curr2.left) or (not curr1.right and curr2.left):
                return False
            if (curr1 and not curr2) or (not curr1 and curr2):
                return False
            if (curr1 and not curr2) or (not curr1 and curr2):
                return False
            if curr1.right: stack1.append(curr1.right)
            if curr1.left:  stack1.append(curr1.left)
            if curr2.left:  stack2.append(curr2.left)
            if curr2.right: stack2.append(curr2.right)
        
        return True
