class Solution:
    def longestPalindrome(self, s: str) -> str:
        # def solve(i,j):
        #     if i >= n or j >= n:
        #         return 0
        #     if dp[i][j] != 0:
        #         return dp[i][j]
        #     if s[i] == s2[j]:
        #         dp[i][j] = 1+solve(i+1,j+1)
        #     else:
        #         dp[i][j] = max(solve(i+1,j) , solve(i,j+1))
        #     return dp[i][j]
        # n = len(s)
        # dp = [[0 for _ in range(n)] for _ in range(n)]
        # s2 = s[::-1]
        # solve(0,0)
        # ans = []
        # i,j = n-1,n-1
        # while i >= 0 and j >= 0:
        #     if s[i] == s2[j]:
        #         ans.append(s[i])
        #         i -= 1
        #         j -= 1
        #     elif dp[i-1][j] > dp[i][j-1]:
        #         i -= 1
        #     else:
        #         j -= 1
        # ans.reverse()
        # return "".join(ans)

        n = len(s)
        
        dp = [[False]*n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = True
            ans = s[i]
            
        maxLen = 1
        
        for start in range(n-1,-1,-1):
            for end in range(start+1,n):
                if s[start] == s[end]:
                    if end-start == 1 or dp[start+1][end-1]:
                        dp[start][end] = True
                        if maxLen < (end-start+1):
                            maxLen = (end-start+1)
                            ans = s[start:end+1]
        return ans

        
        