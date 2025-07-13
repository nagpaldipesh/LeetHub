class Solution:
    def appendCharacters(self, s: str, t: str) -> int:

        index = 0
        for c in s:
            if t[index] == c:
                index+=1
            
            if index == len(t):
                return 0
            
        return  len(t) - index
        