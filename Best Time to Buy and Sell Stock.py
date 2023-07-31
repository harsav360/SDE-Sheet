Problem Link -> https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/


def maxProfit(self, prices: List[int]) -> int:
        # Brute Force Approach -> O(N^2)

        # max_profit = 0
        # for i in range(len(prices)):
        #     profit = 0
        #     for j in range(i+1,len(prices)):
        #         profit = prices[j] - prices[i]
        #         max_profit = max(max_profit,profit)

        # return max_profit
        
        max_profit,profit,miniDay = 0,0,prices[0]

        for i in range(len(prices)):
            profit = prices[i] - miniDay
            max_profit = max(max_profit,profit)
            miniDay = min(miniDay,prices[i])

        return max_profit # Optimal Solution -> T:C -> O(N)
