# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result=0
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(root,mini,maxi):
            if not root:
                self.result=max(self.result,maxi-mini)
                print(self.result)
                return root

            mini = min(mini,root.val)
            maxi = max(maxi,root.val)

            dfs(root.left,mini,maxi)
            dfs(root.right,mini,maxi)
            

        dfs(root,float('inf'),0)

        return self.result