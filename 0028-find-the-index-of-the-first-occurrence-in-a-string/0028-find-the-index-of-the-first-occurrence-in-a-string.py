# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
        # left,right,nedLen = 0,0,len(needle)
        # ptr = 0
        # while right < len(haystack):
        #     if haystack[right] == needle[ptr]:
        #         ptr += 1
        #         right += 1
        #     else:
        #         left += 1
        #         right = left
        #         ptr = 0
        #     if ptr == nedLen:
        #         return left
        # return -1

        # KMP Algorithm
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        lps = [0] * len(needle)

        prevLPS, i = 0, 1
        while i < len(needle):
            if needle[i] == needle[prevLPS]:
                lps[i] = prevLPS + 1
                prevLPS += 1
                i += 1
            elif prevLPS == 0:
                lps[i] = 0
                i += 1
            else:
                prevLPS = lps[prevLPS - 1]

        i = 0  # ptr for haystack
        j = 0  # ptr for needle
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i, j = i + 1, j + 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j - 1]
            if j == len(needle):
                return i - len(needle)
        return -1


        