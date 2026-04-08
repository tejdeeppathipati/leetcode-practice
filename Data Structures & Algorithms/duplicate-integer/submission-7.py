class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       setme = set()
       for x in nums:
        if x in setme:
            return True
        setme.add(x)
       return False     

        