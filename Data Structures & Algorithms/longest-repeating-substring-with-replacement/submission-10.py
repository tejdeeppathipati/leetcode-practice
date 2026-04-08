class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hmap = {}
        res = 0
        maxR = 0
        l = 0
        for r in range(len(s)):
            hmap[s[r]] = 1 + hmap.get(s[r], 0)
            maxR = max(maxR, hmap[s[r]])
            while r - l + 1 - maxR > k:
                hmap[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res 
