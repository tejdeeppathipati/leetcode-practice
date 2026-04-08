# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        out = self.sorting(pairs, 0, len(pairs) - 1)
        return out
    
    def sorting(self, pairs, s, e):
        if e - s + 1 <= 1:
            return pairs
        
        pivot = pairs[e]
        swap = s

        for i in range(s, e):
            if pairs[i].key < pivot.key:
                temp = pairs[swap]
                pairs[swap] = pairs[i]
                pairs[i] = temp
                swap += 1 
        
        pairs[e] = pairs[swap]
        pairs[swap] = pivot

        self.sorting(pairs, s, swap - 1)
        self.sorting(pairs, swap + 1, e)

        return pairs
