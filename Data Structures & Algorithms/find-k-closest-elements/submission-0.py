class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        out = []
        if len(arr) == k:
            return arr
        left, right = 0, len(arr) - 1
        while (right - left) >= k:
            if abs(arr[left] - x) > abs(arr[right] - x):
                left += 1
            elif abs(arr[left] - x) <= abs(arr[right] - x):
                right -= 1
        return arr[left : right + 1]