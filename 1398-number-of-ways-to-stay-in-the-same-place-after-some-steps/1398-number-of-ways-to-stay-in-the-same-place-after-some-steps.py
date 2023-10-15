class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        # def solution(steps,flag):
        #     if steps == 0:
        #         return 0
        #     leftMove,rightMove,noMove = 0,0,0
        #     noMove = 1 + solution(steps-1,flag)
        #     if flag: # If flag is 1, Means I have to move left
        #         leftMove = 1 + solution(steps-1,0)
        #     else:
        #         rightMove = 1 + solution(steps-1,1)
        #     return noMove + leftMove + rightMove

        
        # return solution(steps,0)

        m = steps
        n = min(steps,arrLen)
        dp = [[0]*(n+1) for _ in range(m+1)]
        mod = 10**9+7
        dp[0][0] = 1
        for i in range(1,m+1):
            for j in range(n):
                dp[i][j] = dp[i-1][j+1] + dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i-1][j-1]
        return dp[m][0]%mod
            
            

        