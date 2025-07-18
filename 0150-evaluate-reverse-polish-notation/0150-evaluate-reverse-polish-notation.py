class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                b = stack.pop()
                a = stack.pop()

                s = a + b
                stack.append(s)
            elif token == "-":
                b = stack.pop()
                a = stack.pop()

                s = a - b
                stack.append(s)
            elif token == '*':
                b = stack.pop()
                a = stack.pop()

                m = b * a
                stack.append(m)
            elif token == '/':
                b = stack.pop()
                a = stack.pop()

                d = a / b
                stack.append(int(d))
            else:
                stack.append(int(token))

        return stack.pop()
