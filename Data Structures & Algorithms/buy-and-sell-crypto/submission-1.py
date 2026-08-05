class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = cur = 0
        min_value = prices[0]
        for i in range(1,len(prices)):
            if prices[i] < min_value:
                min_value = prices[i]
            
            cur = prices[i] - min_value
            max_profit = max(max_profit, cur)
        return max_profit


