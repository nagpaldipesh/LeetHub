class Solution:
    def appendCharacters(self, s: str, t: str) -> int:

        index = 0
        n = len(t)

        for c in s:
            if t[index] == c:
                index+=1
            
            if index == n:
                return 0
            
        return  n - index
        