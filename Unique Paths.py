Problem Link -> https://leetcode.com/problems/unique-paths/description/


def uniquePaths(self, m: int, n: int) -> int:

        # def solve(i,j):
        #     if i == m-1 and j == n-1:
        #         return 1
        #     if i >=m or j >= n:
        #         return 0
        #     if dp[i][j] != -1:
        #         return dp[i][j]
        #     right = solve(i,j+1)
        #     down = solve(i+1,j)
        #     dp[i][j] = right + down
        #     return dp[i][j]


        # dp = [[-1 for _ in range(n)] for _ in range(m)]
        # return solve(0,0)

        # Optimal Approach -> T:C = O(M-1) or O(N-1) an S:C -> O(1)

        first = m+n-2
        ans = 1
        for i in range(m-1):
            ans *= (first - i)
            ans //= (i+1)
        return ans
