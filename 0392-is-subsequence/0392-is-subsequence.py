class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True

        index = 0
        n = len(s)

        for c in t:
            if c == s[index]:
                index += 1
            if index == n:
                return True
        
        return False
        