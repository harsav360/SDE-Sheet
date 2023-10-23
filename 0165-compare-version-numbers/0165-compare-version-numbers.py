class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # i,j = 0,0
        # firstLen,secondLen = len(version1),len(version2)
        # nums1,nums2 = 0,0
        # while i < firstLen and j < secondLen:
        #     while i < firstLen and version1[i] != "." : 
        #         nums1 = nums1*10 + int(version1[i])
        #         i += 1
        #     while  j < secondLen and version2[j] != '.':
        #         nums2 = nums2*10 +int(version2[j])
        #         j += 1
        #     if nums1 > nums2:
        #         return 1
        #     elif nums1 < nums2:
        #         return -1
        #     else:
        #         nums1,nums2 = 0,0
        #         i += 1
        #         j += 1
        # while  i < firstLen and version1[i] != '.' :
        #     nums1 = nums1*10 + int(version1[i])
        #     i += 1
        # while j < secondLen and version2[j] != '.' :
        #     nums2 = nums2*10 + int(version2[j])
        #     j += 1
        # if nums1 > nums2:
        #     return 1
        # elif nums1 < nums2:
        #     return -1
        # else:
        #     nums1 = 0
        #     nums2 = 0
        #     i += 1
        #     j += 1
        # while i < firstLen:
        #     while i < firstLen and version1[i] != '.' :
        #         nums1 = nums1*10 + int(version1[i])
        #         i += 1
        #     if nums1 > 0:
        #         return  1
        #     else:
        #         nums1 = 0
        #         i += 1

        # while j < secondLen:
        #     while j < secondLen and version2[j] != '.':
        #         nums2 = nums2*10 + int(version2[j])
        #         j += 1
        #     if nums2 > 0:
        #         return  -1
        #     else:
        #         nums2 = 0
        #         j += 1
        # return 0

        # Optimized Approach

        v1,v2 = list(map(int,version1.split('.'))),list(map(int,version2.split('.')))
        for rev1,rev2 in zip_longest(v1,v2,fillvalue = 0):
            if rev1 == rev2:
                continue
            return -1 if rev1 < rev2 else 1
        return 0


        


        