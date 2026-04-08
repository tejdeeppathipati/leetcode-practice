class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == 0:
            return False

        i, j = 0, 1
        while j < len(nums):
            if nums[j] == nums[i]:
                    if abs(i - j) <= k:
                        return True
            else:
                if j - i < k: 
                    j += 1
                else:
                    if i + 1 == j:
                        j += 1
                    i += 1    
        return False 
        