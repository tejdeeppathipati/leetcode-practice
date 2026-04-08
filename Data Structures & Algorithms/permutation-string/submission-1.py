class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        l, r = 0, len(s1) - 1
        s1Arr = [0] * 26
        s2Arr = [0] * 26
        for i in range(len(s1)):
            s1Arr[ord(s1[i]) - ord('a')] += 1
            s2Arr[ord(s2[i]) - ord('a')] += 1
        
        while r < len(s2):
            if s1Arr == s2Arr:
                return True
            s2Arr[ord(s2[l]) - ord('a')] -= 1
            l += 1
            r += 1
            if r >= len(s2):
                break
            s2Arr[ord(s2[r]) - ord('a')] += 1    
        return False
                
                

