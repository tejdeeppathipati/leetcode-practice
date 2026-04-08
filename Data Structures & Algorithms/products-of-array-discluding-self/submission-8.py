class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        prefix = 1
        postfix = 1
        for i in range(n-1):
            res[0] = 1
            prefix = prefix * nums[i]
            res[i+1] = prefix
        for i in range(n-1,-1,-1):
            res[i] *= postfix
            postfix = postfix * nums[i]
        return res    
              

        
        
        
                    




        
        




            
        