class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        if n == 0:
            return True

        index = 0
        for c in t:
            if c == s[index]:
                index += 1
            if index == n:
                return True
        
        return False
        