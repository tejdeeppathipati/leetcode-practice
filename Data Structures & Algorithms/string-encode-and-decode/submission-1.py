class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for i in range(len(strs)):
            s += strs[i]
            s += "\u03C0"
        return s

    def decode(self, s: str) -> List[str]:
        final_str = []
        str1 = ''
        for i in range(len(s)):
            if s[i] != "\u03C0":
                str1 += s[i]
            if s[i] == "\u03C0":
                final_str.append(str1)
                str1 = ''
        return final_str



