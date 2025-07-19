class Solution:
    def maxDepth(self, s: str) -> int:
        maxDep = maxSoFar = 0

        for c in s:
            if c == '(':
                maxSoFar += 1
            elif c == ')':
                maxSoFar -= 1
            
            maxDep = max(maxSoFar, maxDep)

        return maxDep