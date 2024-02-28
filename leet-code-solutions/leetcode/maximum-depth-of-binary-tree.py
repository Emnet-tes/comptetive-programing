# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxi=0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        cnt=0
        def traverse(root,cnt):
            if not root :
                self.maxi=max(self.maxi,cnt)
                return
            
            traverse(root.left,cnt+1)
            traverse(root.right,cnt+1)
        traverse(root,0)
        
        return self.maxi
        