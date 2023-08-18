Problem Link -> https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# Brute Force approah can be to store the elements inside an set, and then pushing them back into list, because set only contain unique elemets

# Optimal Appraoch

def removeDuplicates(self, nums: List[int]) -> int:
        i,k = 1,0
        n = len(nums)
        while i < n:
            if nums[k] == nums[i]:
                i += 1
            else:
                k += 1
                nums[k] = nums[i]
                i += 1
        return k+1
