class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        for r in range(len(prices)):
            l = 0
            while l < r:
                maxprofit = max(maxprofit, prices[r] - prices[l])
                l += 1 
        return maxprofit

        