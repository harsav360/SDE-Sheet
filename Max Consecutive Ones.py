Problem Link -> https://leetcode.com/problems/max-consecutive-ones/

def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                ans = max(ans,count)
                count = 0
        ans = max(ans,count)
        return ans
