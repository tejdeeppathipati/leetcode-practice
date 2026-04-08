class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(largest):
            subarray = 0
            curSum = 0 
            for n in nums:
                curSum += n
                if curSum > largest:
                    subarray += 1
                    if subarray + 1 > k:
                        return False
                    curSum = n
            return True

        l, r = max(nums), sum(nums)
        res = r
        while l <= r: 
            mid = (r - l)//2 + l
            if canSplit(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res


                
            

        


