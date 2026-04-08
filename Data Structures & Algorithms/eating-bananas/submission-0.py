class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right
        while left <= right:
            mid = (right - left)//2 + left
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(pile/mid)
            if totalTime <= h:
                res = mid
                right = mid - 1
            else: 
                left = mid + 1
        return res

