class Solution:
    def calPoints(self, operations: List[str]) -> int:
        total = 0
        newArr = [] 
        for i in range(len(operations)):
            if operations[i] == "+":
                x = newArr[-1] + newArr[-2]
                newArr.append(x)
            elif operations[i] == "C":
                newArr.pop()
            elif operations[i] == "D":
                x = newArr[-1]
                x = 2 * x
                newArr.append(x)
            else:
                newArr.append(int(operations[i]))
        return sum(newArr)
            
        