class Solution:
    def minOperations(self, s: str) -> int:
        return min(
            self.getMinOperations(s, True),
            self.getMinOperations(s, False)
            )
        
    def getMinOperations(self, s: str, isZero: bool) -> int:
        changesRequired = 0

        for c in s:
            
            if isZero and c == '1':
                changesRequired += 1
            elif not isZero and c == '0':
                changesRequired += 1

            isZero = not isZero

        return changesRequired