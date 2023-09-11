class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # # Simple Brute Force - Sort the array
        # mp,index = {},0
        # for i in nums:
        #     mp[i] = index
        #     index += 1
        # nums.sort()
        # low,high = 0,len(nums)-1
        # while low <= high:
        #     mid = (low+high)//2
        #     if nums[mid] == target:
        #         return mp[nums[mid]]
        #     elif nums[mid] > target:
        #         high = mid-1
        #     else:
        #         low = mid+1
        # return -1

        # Using Extra space to sotre the list elements in sorted array
        # breakPoint = -1
        # mp,index = {},0
        # for i in nums:
        #     mp[i] = index
        #     index += 1
        # for i in range(1,len(nums)):
        #     if nums[i-1] > nums[i]:
        #         breakPoint = i
        #         break
        # temp = []
        # index = breakPoint
        # while index < len(nums):
        #     temp.append(nums[index])
        #     index += 1
        # index = breakPoint-1
        # while index >= 0:
        #     temp.append(nums[index])
        #     index -= 1
        # low,high = 0,len(nums)-1
        # while low <= high:
        #     mid = (low+high)//2
        #     if temp[mid] == target:
        #         return mp[temp[mid]]
        #     elif temp[mid] > target:
        #         high = mid-1
        #     else:
        #         low = mid+1
        # return -1

        # Binary Search Approach

        low,high = 0,len(nums)-1
        while low <= high:
            mid = (low+high) >> 1
            if nums[mid] == target:
                return mid
            # Check, Is left Half Sorted
            if (nums[low] <= nums[mid]):
                if (nums[low] <= target <= nums[mid]):
                    high = mid-1
                else:
                    low = mid+1
            else:
                if (nums[mid] <= target <= nums[high]):
                    low = mid+1
                else:
                    high = mid-1
        return -1
        
        


        
        