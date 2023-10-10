class Solution:
    def minOperations(self, nums: List[int]) -> int:
        length = len(nums)
        nums = sorted(set(nums))
        right = 0
        res = length
        for left in range(len(nums)):
            while right < len(nums) and nums[right] < nums[left]+length:
                right += 1
            window = right-left
            res = min(res,length-window)
        return res
        