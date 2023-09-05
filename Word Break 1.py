Problem Link -> https://leetcode.com/problems/word-break/

def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # Recursion + Memoization Solution

        # def solve(s):
        #     if len(s) == 0:
        #         return True
        #     if s in memo:
        #         return memo[s]
        #     for i in range(len(s)):
        #         first = s[:i+1]
        #         second = s[i+1:]
        #         if first in wordDict:
        #             if second in wordDict:
        #                 return True
        #             else:
        #                 memo[second] = solve(second)
        #                 if memo[second] == True:
        #                     return True

        #         elif second in wordDict:
        #             memo[first] = solve(first)
        #             if memo[first] == True:
        #                 return True
        #     return False

        # memo = {}

        # return solve(s)

        dp = [False]*(len(s)+1)
        dp[0] = True
        for i in range(1,len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]
