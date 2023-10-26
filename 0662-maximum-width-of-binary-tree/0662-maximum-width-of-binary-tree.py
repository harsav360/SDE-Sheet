from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        ans = 0
        que = deque()
        que.append((root,0))
        while que:
            size = len(que)
            mmin = que[0][1]
            first,last = 0,0
            for i in range(size):
                node,curr_id = que.popleft()
                curr_id -= mmin
                if i == 0:
                    first = curr_id
                if i == size-1:
                    last = curr_id
                if node.left != None:
                    que.append((node.left,curr_id*2+1))
                if node.right != None:
                    que.append((node.right,curr_id*2+2))
            ans = max(ans,last-first+1)
        return ans

        
