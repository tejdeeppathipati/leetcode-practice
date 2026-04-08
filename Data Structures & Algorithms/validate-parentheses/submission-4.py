class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {"}" : "{", ")" : "(", "]" : "["}
        stack = []
        opener = set(hashmap.values())
        for i in range(len(s)):
            if s[i] in opener:
                stack.append(s[i])
            else:
                if stack and (hashmap[s[i]] == stack[-1]):
                    stack.pop()
                else:
                    return False
        return stack == []
        

        
