# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def Calc(child, parent, val, depth):
            if not child:
                return None
            if child.val == val:
                return (depth,parent)
            return Calc(child.left,child,val,depth+1) or Calc(child.right,child,val,depth+1)
        
        Xdepth, Xparent = Calc(root ,None, x, 0)
        Ydepth, Yparent = Calc(root,None, y, 0) 

        return Xdepth == Ydepth and Xparent != Yparent
        