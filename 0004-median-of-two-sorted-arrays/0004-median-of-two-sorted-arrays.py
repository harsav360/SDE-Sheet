class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Brute Force Approach
        # Time Complexity -> O(len(nums1) + len(nums2))
        # Space Complexity -> O(len(nums1) + len(nums2))
        temp = []
        i,j = 0,0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                temp.append(nums1[i])
                i += 1
            else:
                temp.append(nums2[j])
                j += 1
        while i < len(nums1):
            temp.append(nums1[i])
            i += 1
        while j < len(nums2):
            temp.append(nums2[j])
            j += 1
        comLen = len(temp)
        if comLen%2 != 0:
            ans = temp[comLen//2]
        else:
            ans = temp[comLen//2] + temp[comLen//2-1]
            ans = ans/2
        ans = ans/1
        return ans

        