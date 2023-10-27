# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root == None:
            return ans
        que = deque()
        que.append(root)
        flag = 1
        while que:
            flag = 1-flag
            length = len(que)
            temp = []
            for i in range(length):
                node = que.popleft()
                temp.append(node.val)
                # if the flag is 1, right to left
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            if flag:
                ans.append(temp[::-1])
            else:
                ans.append(temp)
        return ans



        