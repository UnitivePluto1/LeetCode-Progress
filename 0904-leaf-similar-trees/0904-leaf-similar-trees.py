# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def findLeafArr(root, array):
            if not root:
                return 
            if not root.left and not root.right:
                array.append(root.val)
            else:
                findLeafArr(root.left, array)
                findLeafArr(root.right, array)

        Leaf1 =  []
        findLeafArr(root1, Leaf1)
        Leaf2 = []
        findLeafArr(root2, Leaf2)

        return Leaf1 == Leaf2