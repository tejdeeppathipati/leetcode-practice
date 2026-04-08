class Solution:
    def findMin(self, nums: List[int]) -> int:
        minNum = nums[0] 
        left = 0 
        right = len(nums) - 1
        # [3,4,5,6,1,2]
        while left < right:
            mid = ((right - left)//2) + left 
            if nums[mid] > nums[right]:
                minNum = nums[mid + 1]
                left = mid + 1
            if nums[mid] < nums[right]:
                minNum = nums[mid]
                right = mid
        return minNum
