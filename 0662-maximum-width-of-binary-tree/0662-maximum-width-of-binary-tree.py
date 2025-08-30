# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([(root,0)])
        maxWidth = 0

        while q:
            length = len(q)
            _, start = q[0]

            for i in range(length):
                node, idx = q.popleft()

                if node.left:
                    q.append((node.left, 2*idx+1))
                if node.right:
                    q.append((node.right, 2*idx+2))
            maxWidth = max(maxWidth, idx - start + 1)
        return maxWidth