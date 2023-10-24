# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        que = deque()
        ans = []
        if root == None:
            return ans
        que.append((root,0))
        while que:
            maxi = float('-inf')
            for _ in range(len(que)):
                node,level = que.popleft()
                if node.val > maxi:
                    maxi = node.val
                if node.left:
                    que.append((node.left,level+1))
                if node.right:
                    que.append((node.right,level+1))
            ans.append(maxi)
        return ans
        