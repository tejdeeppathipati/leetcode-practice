class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = self.minfinder(nums)
        left, right = 0, len(nums) - 1
        if index != 0:
            if nums[index] <= target <= nums[right]:
                left, right = index, right
            else:
                left, right = 0 , index - 1
        while left <= right:
            mid = (right - left)//2 + left
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target:
                return mid
        return -1
    
    def minfinder(self, nums): # min finder
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (right - left)//2 + left
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
        return left  
