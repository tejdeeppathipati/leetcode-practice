class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        if len(tokens) != 0:
            for i in range(len(tokens)):
                if tokens[i] in ["+","/","*","-"]:
                    if tokens[i] == "+":
                        result = (stack.pop() + stack.pop())
                    elif tokens[i] == "*":
                        result = (stack.pop() * stack.pop())
                    elif tokens[i] == "-":
                        a, b = stack.pop(), stack.pop()
                        result = b - a
                    elif tokens[i] == "/":
                        a, b = stack.pop(), stack.pop()
                        result = int(b / a)
                    stack.append(result)
                else:
                    stack.append(int(tokens[i]))
        return int(stack[0])
                



                
                
        