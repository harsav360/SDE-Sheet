class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # ans = []
        # for i in range(len(nums1)):
        #     flag = 0
        #     app = 0
        #     for j in range(len(nums2)):
        #         if nums1[i] == nums2[j]:
        #             flag = 1
        #         if flag == 1 and nums2[j] > nums1[i]:
        #             ans.append(nums2[j])
        #             app = 1
        #             break
        #     if flag == 0 or app == 0:
        #         ans.append(-1)
        # return ans
        
        # stack = []
        # ans = []
        # for num in nums2:
        #     stack.append(nums2.pop())
        # for i in nums1:
        #     temp = stack[:]
        #     flag = 0
        #     while temp:
        #         ele = temp.pop()
        #         if ele == i:
        #             flag = 1
        #         if flag == 1 and ele > i:
        #             ans.append(ele)
        #             break
        #     if len(temp) == 0:
        #         ans.append(-1)
        # return ans

        # Efficient Solution

        nums1Idx = {n:i for i,n in enumerate(nums1)}
        res = [-1]*len(nums1)
        stack  = []

        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and stack[-1] < cur:
                val = stack.pop()
                idx = nums1Idx[val]
                res[idx] = cur
            if cur in nums1Idx:
                stack.append(cur)
        return res

            

        