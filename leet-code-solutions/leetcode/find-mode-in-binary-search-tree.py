# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        visited=[]
        #to keep track of maximum occurunce
        d=defaultdict(int)
        self.maxi=0
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            visited.append(root.val)
            d[root.val]+=1
            self.maxi=max(self.maxi,d[root.val])
            inorder(root.right)
        inorder(root)
        ans=[]
        #for elemnts with maximum occurenc
        for n in d.keys():
            if d[n]==self.maxi:
                ans.append(n)
        return ans
        