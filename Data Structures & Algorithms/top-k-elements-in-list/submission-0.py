class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fmap = Counter(nums)

        bucket = [[] for _ in range(len(nums)+1)]

        # [[],[],[],[]]

        for num, freq in fmap.items():
            bucket[freq].append(num)
        
        res = []
        for i in range(len(bucket)-1, 0, -1):
            res.extend(bucket[i])
            if len(res) >= k:
                return res[:k]

        







            

                      

        