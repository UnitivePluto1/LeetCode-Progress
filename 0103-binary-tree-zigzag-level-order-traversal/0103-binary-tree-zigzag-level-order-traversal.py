# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        q.append(root)
        ans = []
        lefttoright = True
        while q:
            size = len(q)
            group = [0]*size

            for i in range(size):
                node = q.popleft()
                idx = i if lefttoright else size - 1 - i
                group[idx] = node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(group)
            lefttoright = not lefttoright
        return ans