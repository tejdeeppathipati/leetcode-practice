class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)
        output = ""
        for i in range(max(l1, l2)):
            if i in range(l1):
                output += word1[i]
            if i in range(l2):
                output += word2[i]
        return output 