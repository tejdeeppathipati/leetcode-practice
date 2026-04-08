class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0 , x
        while l <= r:
            m = (r - l)//2 + l 
            if m * m == x:
                return m
            elif m*m > x:
                r = m - 1
            else:
                if (m+1) * (m+1) > x:
                    return m
                l = m + 1
        return -1