# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # def solve(root,firstNode,secondNode,p,q):
        #     if root == None:
        #         return
        #     if root == p:
        #         firstNode = True
        #     if root == q:
        #         secondNode = True
        #     if firstNode == True and secondNode == True:
        #         ans[0] = root
        #         return
        #     solve(root.left,firstNode,secondNode,p,q)
        #     solve(root.right,firstNode,secondNode,p,q)

        # ans = [root]
        # solve(root,False,False,p,q)
        # return ans[0]

        """ Brute Force Approach
        1. First Calculate the path of both nodes and store the result in 
        some array or list.
        2. Then start compairing the array list one by one, and stop when there is no match, then the last matched result is our answer.
        """


        def findPath(root,path,target):
            if root == None:
                return False
            path.append(root)
            if root == target:
                return True
            
            if findPath(root.left,path,target) or findPath(root.right,path,target):
                return True
            path.pop()
            return False
        firstNodePath = []
        findPath(root,firstNodePath,p)
        secondNodePath = []
        findPath(root,secondNodePath,q)
        length = min(len(firstNodePath),len(secondNodePath))
        ans = None
        for i in range(length):
            if firstNodePath[i] == secondNodePath[i]:
                ans = firstNodePath[i]
            else:
                break
        return ans




        