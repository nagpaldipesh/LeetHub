class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []

        for c in s:
            if stack and c.isdigit():
                stack.pop()
                continue

            stack.append(c)

        return ''.join(stack)