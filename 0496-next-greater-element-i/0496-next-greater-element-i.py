class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums1)):
            flag = 0
            app = 0
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    flag = 1
                if flag == 1 and nums2[j] > nums1[i]:
                    ans.append(nums2[j])
                    app = 1
                    break
            if flag == 0 or app == 0:
                ans.append(-1)
        return ans
        
        