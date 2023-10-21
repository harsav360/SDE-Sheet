class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = strs[0]
        for i in range(1,len(strs)):
            n = len(strs[i])
            actLen = len(ans)
            j,k = 0,0
            while j < n and k < actLen:
                if ans[k] != strs[i][j]:
                    break
                else:
                    k += 1
                    j += 1
            ans = strs[i][:j]
        return ans
                


        