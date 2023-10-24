# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # def inorder(root):
        #     if root:
        #         inorder(root.left)
        #         result.append(root.val)
        #         inorder(root.right)
        
        # result = []
        # inorder(root)
        # return result

        # Morris Inorder Traversal

        ans = []
        cur = root
        while cur != None:
            if cur.left == None:
                ans.append(cur.val)
                cur = cur.right
            else:
                prev = cur.left
                while prev.right and prev.right != cur:
                    prev = prev.right
                if prev.right == None:
                    prev.right = cur
                    cur = cur.left
                else:
                    prev.right = None
                    ans.append(cur.val)
                    cur = cur.right
        return ans
        
        