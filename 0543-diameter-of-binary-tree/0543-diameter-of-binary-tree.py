# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def solve(root):
            if root == None:
                return 0
            left_path = solve(root.left)
            right_path = solve(root.right)
            maxAns[0] = max(maxAns[0],left_path+right_path)
            return 1 + max(left_path,right_path)
        maxAns = [float('-inf')]
        solve(root)
        return maxAns[0]

        