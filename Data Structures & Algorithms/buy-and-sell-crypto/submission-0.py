class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = cur = 0
        for i in range(1,len(prices)):
            cur = prices[i] - min(prices[:i])
            max_profit = max(max_profit, cur)
        return max_profit


