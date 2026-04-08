class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        count = 0 
        l = 0 
        for r in range(len(s)):
            if s[r] in hashmap:
                count = max(count, r - l)
                l = max(l, hashmap[s[r]] + 1)
            else:
                count = max(count, r - l)
            hashmap[s[r]] = r 
        count = max(count, len(s) - l)
        return count              