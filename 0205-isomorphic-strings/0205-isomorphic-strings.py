class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        if(n != len(t)):
            return False

        maps = {}
        mapt = {}

        for i in range(n):
            key1 = s[i]
            key2 = t[i]
            
            if key1 in maps and maps[key1] != key2:
                return False
            elif key2 in mapt and mapt[key2] != key1:
                return False
            else:
                maps[key1] = key2
                mapt[key2] = key1
            
        return True