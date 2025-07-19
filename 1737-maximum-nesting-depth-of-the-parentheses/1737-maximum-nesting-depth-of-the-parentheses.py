class Solution:
    def maxDepth(self, s: str) -> int:
        maxDep = maxSoFar = 0

        for c in s:
            if c == '(':
                maxSoFar += 1
                maxDep = max(maxSoFar, maxDep)
            elif c == ')':
                maxSoFar -= 1
            
        return maxDep