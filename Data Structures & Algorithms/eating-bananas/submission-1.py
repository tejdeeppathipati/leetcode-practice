class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        minNumber = max(piles)
        while l <= r:
            mid = (l + r) // 2
            totalTime = 0 
            for i in range(len(piles)):
                totalTime += math.ceil(piles[i] / mid)
            if totalTime <= h:
                minNumber = mid
                r = mid - 1
            else:
                l = mid + 1
        return minNumber
            