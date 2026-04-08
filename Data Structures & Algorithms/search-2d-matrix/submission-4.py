class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        for row in matrix:
            if row[0] <= target <= row[-1]:
                l,r = 0,(len(row) - 1)
                while l <= r:
                    mid = ((r - l)//2) + l
                    if row[mid] < target:
                        l = mid + 1
                    elif row[mid] == target:
                        return True
                    else:
                        r = mid - 1
        return False

