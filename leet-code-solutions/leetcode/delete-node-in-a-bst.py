# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def delete(root,key):
            if not root:
                return root
            if root.val>key:
                root.left=delete(root.left,key)
            elif root.val<key:
                root.right=delete(root.right,key)
            else:
                #found the key to be deleted
                if not root.right:
                    return root.left
                elif not root.left:
                    return root.right
                #found the inorder succesor
                temp=in_succesor(root.right)
                #swap values
                root.val=temp.val
                root.right=delete(root.right,temp.val)
            return root
        def in_succesor(node):
            cur=node
            while cur.left:
                cur=cur.left
            return cur
        return delete(root,key)


            