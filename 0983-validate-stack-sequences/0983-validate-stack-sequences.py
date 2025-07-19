class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        n = len(pushed)
        if n != len(popped):
            return False

        stack = []
        index = 0
        p = 0
        while index < n:
            stack.append(pushed[index])
            #print(stack)
            while stack and stack[-1] == popped[p]:
                stack.pop()
                p += 1

            index += 1

        return len(stack) == 0