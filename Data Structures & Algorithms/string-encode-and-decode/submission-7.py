class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for word in strs:
            encoded += str(len(word)) + "#" + word 
        return encoded

    def decode(self, s: str) -> List[str]:
        final = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j = j + 1
            length = int(s[i : j])
            word = s[j+1 : j+1+length]
            i = j+1+length 
            final.append(word)
        return final 