class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L  = 0
        R = len(numbers) - 1
        for i in range(len(numbers)):
            if numbers[L] + numbers[R] > target:
                R-=1
            elif numbers[L] + numbers[R] < target:
                L+=1
            else :
                numbers[L] + numbers[R] == target
                return [L+1,R+1]        

        

        