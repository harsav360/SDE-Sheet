Given an integer array nums, find the 
subarray with the largest sum, and return its sum.

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

def maxSubArray(self, nums: List[int]) -> int:
        # ans = float('-inf')
        # for i in range(len(nums)):
        #     temp = 0
        #     for j in range(i,len(nums)):
        #         temp += nums[j]
        #         ans = max(ans,temp)

        # return ans # Brute Force -> T:C -> O(N^2)

        ans = float('-inf')
        temp = 0
        for i in range(len(nums)):
            temp += nums[i]
            ans = max(ans,temp)
            if temp < 0:
                temp = 0

        return ans  # Optimal T:C -> O(N)
