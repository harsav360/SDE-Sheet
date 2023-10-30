# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(before,after):
            if before == None or after == None:
                return before == after
            if before.val != after.val:
                return False
            return check(before.left,after.right) and check(before.right,after.left)


        if root == None:
            return True
        return check(root.left,root.right)        