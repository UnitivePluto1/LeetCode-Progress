# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.grid = []
        def assign(node,row,col):
            if not node:
                return 
            self.grid.append([col,row,node.val])
            assign(node.left, row+1, col-1)
            assign(node.right, row+1, col+1)

        assign(root, 0, 0)


        #(tup[0] for tup in self.grid)

        col_map = defaultdict(list)

        self.grid.sort()

        for col,row,val in self.grid:
            col_map[col].append(val)
        
        return [col_map[c] for c in sorted(col_map)]