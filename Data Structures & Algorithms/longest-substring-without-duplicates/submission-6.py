class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        output,l = 0, 0 
        hashmap = {} 
        for r in range(len(s)):
            if s[r] in hashmap:
                l = max(hashmap[s[r]] +  1, l)
            hashmap[s[r]] = r
            output = max(output, r - l + 1)
        return output

            