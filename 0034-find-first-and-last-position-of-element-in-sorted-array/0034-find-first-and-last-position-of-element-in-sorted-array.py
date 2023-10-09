class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        firstPos,secondPos = -1,-1
        low,high = 0,len(nums)-1

        # First find Start
        while low <= high:
            mid = (low+high)//2

            if nums[mid] == target:
                firstPos = mid
                high = mid-1
            elif nums[mid] > target:
                high = mid-1
            else:
                low = mid+1

        # Then find last Position
        low,high = 0,len(nums)-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                secondPos = mid
                low = mid+1
            elif nums[mid] > target:
                high = mid-1
            else:
                low = mid+1
        return [firstPos,secondPos]

        