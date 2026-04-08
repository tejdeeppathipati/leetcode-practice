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
                newArr.append(2 * newArr[-1])
            else:
                newArr.append(int(operations[i]))
        return sum(newArr)
            
        