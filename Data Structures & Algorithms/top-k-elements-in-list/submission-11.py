class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        newhash = {}
        for i in nums:
            if i not in newhash:
                newhash[i] = 0
            newhash[i] +=1
        sorted_dict = dict(sorted(newhash.items(), key=lambda x: x[1], reverse=True))
        keys = list(sorted_dict.keys())
        new_arr = keys[:k]
        return new_arr


        


        