class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) == 1:
             return 0
        
        # maxprofit = 0
        # for i in range (len(prices)-1):
        #     for j in range(i+1, len(prices)):
        #         if prices[i] < prices[j]:
        #             profit = prices[j] - prices[i]
        #             maxprofit = max (maxprofit, profit)

        # return maxprofit

        buyItem = prices[0]
        profit = 0

        for p in prices[1:]:
            if p < buyItem:
                buyItem = p
            profit = max (profit , p - buyItem)
        
        return profit
