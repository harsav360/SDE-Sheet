# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # mp = defaultdict(list)
        # que = deque()
        # que.append((root,0))
        # while que:
        #     node,level = que.popleft()
        #     mp[level].append(node.val)
        #     if node.right:
        #         que.append((node.right,level+1))
        #     if node.left:
        #         que.append((node.left,level-1))
        # result = []
        # for key in sorted(mp.keys()):
        #     result.append(sorted(mp[key]))
        # return result

        def helper(placement,level,root,dic):
            if root == None:
                return
            dic[placement].append((level,root.val))
            helper(placement-1,level+1,root.left,dic)
            helper(placement+1,level+1,root.right,dic)

        dic = defaultdict(list)
        helper(0,0,root,dic)
        result = []
        for i in sorted(dic.keys()):
            temp = []
            for j in sorted(dic[i]):
                temp.append(j[1])
            result.append(temp)
        return result

        