class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        left,right,nedLen = 0,0,len(needle)
        ptr = 0
        while right < len(haystack):
            if haystack[right] == needle[ptr]:
                ptr += 1
                right += 1
            else:
                left += 1
                right = left
                ptr = 0
            if ptr == nedLen:
                return left
        return -1

        