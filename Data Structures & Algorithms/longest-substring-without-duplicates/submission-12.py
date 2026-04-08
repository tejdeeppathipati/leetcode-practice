class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hmap = {}
        maxL = 0
        l = 0
        for r in range(len(s)):
            if s[r] in hmap:
                l = max(hmap[s[r]] + 1, l)
            hmap[s[r]] = r
            maxL = max(maxL, r - l + 1)
        return maxL
                