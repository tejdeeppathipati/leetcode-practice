class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        output = []
        for i in range(max(len1, len2)):
            if i in range(len1):
                output.append(word1[i])
            if i in range(len2):
                output.append(word2[i])
        return "".join(output)





        