class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        def solve(i,j,flag):
            if i >= n or j >= m:
                if flag == 1:
                    return 0
                return -1
            elif (i,j,flag) in dp:
                return dp[(i,j,flag)]
            op1 = nums1[i]*nums2[j] + solve(i+1,j+1,1)
            op2 = solve(i+1,j,flag)
            op3 = solve(i,j+1,flag)
            dp[(i,j,flag)] = max(op1,op2,op3)
            return dp[(i,j,flag)]
        n,m = len(nums1),len(nums2)
        dp = {}
        check =  solve(0,0,0)
        if check == -1:
            firstMin,firstMax = min(nums1),max(nums1)
            secondMin,secondMax = min(nums2),max(nums2)
            ans = max(firstMin*secondMax,firstMax*secondMin)
            return ans
        return check
        
        