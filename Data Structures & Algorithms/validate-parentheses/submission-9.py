class Solution:
    def isValid(self, s: str) -> bool:
        valid_str = {")": "(", "}": "{", "]": "["}

        stack = []
        for i in s:
            if i in valid_str:
                if not stack:
                    return False
                top = stack.pop()
                if top != valid_str[i]:
                    return False        
               
            else:
                #opening
                stack.append(i)
        if stack:
            return False
        else:
            return True            
