class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        left,right = 0,len(matrix) - 1
        while left <= right:
            mid = (right - left)//2 + left
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                l,r = 0, len(matrix[mid]) - 1
                while l <= r:
                    m = (r - l)//2 + l
                    if matrix[mid][m] >  target:
                        r = m - 1
                    elif matrix[mid][m] < target:
                        l = m + 1
                    elif matrix[mid][m] == target:
                        return True 
                return False
            elif matrix[mid][0] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False 
    
