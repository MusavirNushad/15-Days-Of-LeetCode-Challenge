class Solution:
    def calPoints(self, operations: List[str]) -> int:
        

        res = []

        for i in range(len(operations)):
            if operations[i] == "C":
                res.pop(-1)
            elif operations[i] == "D":
                res.append(res[-1]*2)
            
            elif operations[i] == "+":
                res.append(res[-2] + res[-1])
            else:
                res.append(int(operations[i]))
        
        sum = 0

        for num in res:
            sum+= num
        
        return sum


