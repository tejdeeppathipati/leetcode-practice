class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        buckets = [[] for _ in range(len(nums) + 1) ]
        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)
        for key, value in hashmap.items():
            buckets[value].append(key)
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) >= k:
                    return result
            
            
        
        
        