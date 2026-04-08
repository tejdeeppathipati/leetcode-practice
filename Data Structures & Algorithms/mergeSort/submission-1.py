# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        m = len(pairs) // 2
        if len(pairs) <= 1:
            return pairs

        left = self.mergeSort(pairs[:m])
        right = self.mergeSort(pairs[m:])

        self.merge(pairs, left, right)
        return pairs
    
    def merge(self, pairs, left, right):
        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i].key <= right[j].key:
                pairs[k] = left[i]
                i += 1
                k += 1
            else:
                pairs[k] = right[j]
                j += 1
                k += 1

        while i < len(left):
            pairs[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            pairs[k] = right[j]
            j += 1
            k += 1
        


