Problem Link -> https://leetcode.com/problems/merge-sorted-array/description/

ef merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # ans = []
        # i,j = 0,0
        # while i < m and j < n:
        #     if nums1[i] < nums2[j]:
        #         ans.append(nums1[i])
        #         i += 1
        #     else:
        #         ans.append(nums2[j])
        #         j += 1
        # while i < m:
        #     ans.append(nums1[i])
        #     i += 1
        # while j < n:
        #     ans.append(nums2[j])
        #     j += 1
        # nums1[:] = ans

        # startI,i = m,0
        # while i < n:
        #     nums1[startI+i] = nums2[i]
        #     i += 1
        # nums1.sort()

        # if m == 0:
        #     nums1[:] = nums2
        # if n == 0:
        #     return

        # def swap(ind1,ind2):
        #     if nums1[ind1] > nums2[ind2]:
        #         nums1[ind1],nums2[ind2] = nums2[ind2],nums1[ind1]

        # l = n+m
        # gap = l//2 + l%2
        # while gap > 0:
        #     left = 0
        #     right = left+gap
        #     while right < l:
        #         # left in nums1 and right in nums2
        #         if (left < m and right >= m):
        #             swap(left,right-m)
        #         # left and right both in nums2
        #         elif (left >= m):
        #             swap(left-m,right-m)
        #         # both are in nums1
        #         else:
        #             swap(left,right)
        #         left += 1
        #         right += 1
        #     if gap == 1:
        #         break
        #     else:
        #         gap = gap//2 + gap%2
        # count = 0
        # for i in range(m,l):
        #     nums1[i] = nums2[count]
        #     count += 1

        i,j,k = m-1,n-1,m+n- 1
        while i >= 0 and j >= 0:
            if (nums1[i] < nums2[j]):
                nums1[k] = nums2[j]
                k -= 1
                j -= 1
            else:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1
