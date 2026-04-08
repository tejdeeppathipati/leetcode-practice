class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == 0:
            return False
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = i
            else:
                if abs(hashmap[nums[i]] - i) <= k:
                    return True
                hashmap[nums[i]] = i
        return False