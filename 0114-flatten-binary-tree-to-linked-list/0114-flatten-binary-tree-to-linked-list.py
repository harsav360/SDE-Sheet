# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def solve(root):
            if root == None:
                return
            solve(root.right)
            solve(root.left)
            root.right = prev[0]
            root.left = None
            prev[0] = root

        prev = [None]
        solve(root)
