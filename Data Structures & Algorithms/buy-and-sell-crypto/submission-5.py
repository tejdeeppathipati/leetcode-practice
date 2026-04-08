class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxProfit = 0
        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            maxProfit = max(prices[r] - prices[l], maxProfit)
        return maxProfit
        
            
            
    
        