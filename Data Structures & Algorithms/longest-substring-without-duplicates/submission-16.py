class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, maxL = 0, 0
        hmap = {}
        for r in range(len(s)):
            if s[r] in hmap:
                while l <= hmap[s[r]]:
                    l += 1
            hmap[s[r]] = r
            maxL = max(maxL, r-l+1)
        return maxL

        