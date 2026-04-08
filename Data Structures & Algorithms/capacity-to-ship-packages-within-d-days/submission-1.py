class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left  = max(weights)
        right = sum(weights)
        ouput = 0 
        while left <= right:
            mid = (right - left)//2 + left
            capacity,totalDays = 0,1
            for weight in weights:
                if capacity + weight <= mid:
                    capacity += weight
                else:
                    totalDays += 1
                    capacity = weight
            if totalDays > days:
                left = mid + 1
            else:
                output = mid
                right = mid - 1
        return output



