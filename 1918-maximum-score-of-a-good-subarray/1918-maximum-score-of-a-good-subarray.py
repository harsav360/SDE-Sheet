class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        l = r = k
        ans = nums[k]
        mini,n = nums[k],len(nums)
        while r < n-1 or l > 0:
            left = nums[l-1] if l > 0 else 0
            right = nums[r+1] if r < n-1 else 0
            if left > right:
                l -= 1
                mini = min(mini,left)
            else:
                r += 1
                mini = min(mini,right)
            ans = max(ans,mini*(r-l+1))
        return ans



        