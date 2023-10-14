class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:

        def solution(index,remain):
            if remain <= 0:
                return 0
            if (index,remain) in dp:
                return dp[(index,remain)]
            if index >= n:
                return float('inf')
            paint = cost[index] + solution(index+1,remain-time[index]-1)
            notPaint = solution(index+1,remain)
            dp[(index,remain)] = min(paint,notPaint)
            return min(paint,notPaint)

        n = len(cost)
        dp = {}
        return solution(0,n)

            

        