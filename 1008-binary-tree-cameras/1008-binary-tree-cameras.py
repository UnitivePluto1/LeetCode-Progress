# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        '''
        0 is for a node that isnt covered by the camera
        1 is for a node that has a camera 
        2 is for a node that is covered by a camera but doesnt have a camera on it
        '''
        self.cameras = 0

        def dfs(node):
            if not node:
                return 2
            
            left, right = dfs(node.left), dfs(node.right)

            if left == 0 or right == 0:
                self.cameras += 1
                return 1
            if left == 1 or right == 1:
                return 2
            else:
                return 0

        if dfs(root) == 0:
            self.cameras+=1
        
        return self.cameras

