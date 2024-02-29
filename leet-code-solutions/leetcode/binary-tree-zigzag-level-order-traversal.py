# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=deque()
        ans=[]
        q.append(root)
        front=True
        while q:
            n=len(q)
            level=[]
            for i in range(n):
                temp=q.popleft()
                if temp:
                    level.append(temp.val)
                    q.append(temp.left)
                    q.append(temp.right)
            
            if level and front:
                ans.append(level)
                front=False
            elif level and not front:
                rev=reversed(level)
                ans.append(rev)
                front=True
            
        return ans
