# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(node, row, col):
            if node is None:
                return 
            else:
                if row in ans:
                    ans[row]['min'] = min(ans[row]['min'], col)
                    ans[row]['max'] = max(ans[row]['max'], col)
                else:
                    ans[row] = dict()
                    ans[row]['min'] = col
                    ans[row]['max'] = col
                helper(node.left, row+1, 2*col)
                helper(node.right, row+1, 2*col+1)
                
        ans = dict()

        helper(root, 0, 0)

        max_width=0
        for i in ans.keys():
            max_width = max(max_width, 1+ans[i]['max']-ans[i]['min'])
        return max_width