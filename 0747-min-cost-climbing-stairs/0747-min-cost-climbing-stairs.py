class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # def solution(index,paisa):
        #     if (index >= n):
        #         return paisa
        #     if dp[index] != -1:
        #         return dp[index]
        #     else:
        #         dp[index] =  min(solution(index+1,cost[index]+paisa),solution(index+2,cost[index]+paisa))
        #         return dp[index]

        # n = len(cost)
        # dp = [-1 for _ in range(n)]
        # first = solution(0,0)
        # dp = [-1 for _ in range(n)]
        # second = solution(1,0)
        # return min(first,second)

        def solution(index,cost):
            if index < 0:
                return 0
            if index == 0 or index == 1:
                return cost[index]
            if dp[index] != -1:
                return dp[index]
            dp[index] = cost[index]+min(solution(index-1,cost),solution(index-2,cost))
            return dp[index]

        n = len(cost)
        dp = [-1 for _ in range(n)]
        return min(solution(n-1,cost),solution(n-2,cost))


        