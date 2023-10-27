# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = -1000000

        def calculate(root):
            if root == None:
                return 0
            left = max(0,calculate(root.left))
            right = max(0,calculate(root.right))
            self.ans = max(self.ans,left+right+root.val)
            return max(left,right)+root.val
        check = calculate(root)
        return self.ans
        