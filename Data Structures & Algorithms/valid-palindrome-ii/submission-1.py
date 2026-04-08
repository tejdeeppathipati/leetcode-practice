class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        count = 0
        while l < r:
            if s[l] != s[r] and count < 1 :
                if s[l] == s[r - 1]:
                    r -= 1
                    count += 1
                elif s[l + 1] == s[r]:
                    l += 1
                    count += 1
                else:
                    return False 
            elif s[l] == s[r]:
                r -= 1
                l += 1
            else:
                return False
        return True 
            
        