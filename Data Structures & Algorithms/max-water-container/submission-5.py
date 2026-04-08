class Solution:
    def maxArea(self, heights: List[int]) -> int:
       L = 0
       R = len(heights)-1
       max_count = 0
       while L < R:
        width  =  R - L
        min_me =  min(heights[L],heights[R])
        area = width * min_me
        if area > max_count:
            max_count = area
        if heights[L] < heights[R]:
            L+=1
        else:
            R-=1
       return max_count    
        
        


                
                

                        
                           

        