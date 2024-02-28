# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        visited=[]
        self.flag=True
        def dfs(root):
            if not root:
                return 
            dfs(root.left)
            if visited and visited[-1]>=root.val:
                self.flag=False
            visited.append(root.val)
            dfs(root.right)
        dfs(root)
        return self.flag
        