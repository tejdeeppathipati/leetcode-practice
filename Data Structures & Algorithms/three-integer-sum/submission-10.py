class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        newarr = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = len(nums)-1
            while j<k:
                sums = nums[i] + nums[j] + nums[k];  
                if sums == 0:
                    triplet = [nums[i], nums[j], nums[k]]
                    if triplet not in newarr:
                        newarr.append(triplet)
                    j+=1
                    k-=1
                elif sums < 0:
                    j+=1
                else:
                    k-=1
        return newarr
           


            
        