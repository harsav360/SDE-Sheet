class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Simple Brute Force - Sort the array
        mp,index = {},0
        for i in nums:
            mp[i] = index
            index += 1
        nums.sort()
        low,high = 0,len(nums)-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mp[nums[mid]]
            elif nums[mid] > target:
                high = mid-1
            else:
                low = mid+1
        return -1

        
        