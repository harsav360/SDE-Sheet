# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mt: 'MountainArray') -> int:
        low,high,peak = 1,mt.length()-2,-1
        while low <= high:
            mid = (low+high)//2
            left,middle,right = mt.get(mid-1),mt.get(mid),mt.get(mid+1)
            if left < middle < right:
                low = mid+1
            # Check for left side
            elif left > middle > right:
                high = mid-1
            else:
                break
        peak = mid
        #Binary Search at the left side of Peak
        low,high = 0,peak
        while low <= high:
            mid =   (low+high)//2
            value = mt.get(mid)
            if value == target:
                return mid
            elif value > target:
                high = mid-1
            else:
                low = mid+1
        low,high = peak,mt.length()-1
        while low <= high:
            mid =   (low+high)//2
            value = mt.get(mid)
            if value == target:
                return mid
            elif value < target:
                high = mid-1
            else:
                low = mid+1
        return -1

                       