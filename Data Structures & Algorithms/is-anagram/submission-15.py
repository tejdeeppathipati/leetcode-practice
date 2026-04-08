class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mapfort = {}
        mapfors = {}

        for x in s:
            if x in mapfort:
                mapfort[x] += 1
            else:
                mapfort[x] = 1   
        for y in t:
            if y in mapfors:
                mapfors[y] += 1
            else:
                mapfors[y] = 1

        return mapfort == mapfors
