class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        maxprofit = 0
        l = 0
        for r in range(len(prices)):
            if prices[l] > prices[r]:
                l = r 
            else:
                maxprofit = max(maxprofit, prices[r] - prices[l])
        return maxprofit

        