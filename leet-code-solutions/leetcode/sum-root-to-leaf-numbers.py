# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans=0
        def dfs(root,val):
            if not root: return

            val = (val*10) + root.val

            if not root.left and not root.right:
                self.ans += val
                return  
            dfs(root.left,val)
            dfs(root.right,val)
        dfs(root,0)
        return self.ans
        