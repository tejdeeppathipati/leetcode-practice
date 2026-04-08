class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for word in strs:
            count = [0] * 26
            for j in word:
                count[ord(j) - ord('a')] += 1
            count = tuple(count)

            if count not in result:
                result[count] = []

            result[count].append(word)
            
        return list(result.values())
            
