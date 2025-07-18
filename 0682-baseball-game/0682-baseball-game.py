class Solution:

    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for operation in operations:
            if operation == "C":
                stack.pop()
            elif operation == "D":
                stack.append(stack[-1] * 2)
            elif operation == "+":
                total = stack[-1] + stack[-2]
                stack.append(total)
            else:
                stack.append(int(operation))
        
        return sum(stack)
