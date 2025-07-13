class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        if(n != len(t)):
            return False

        maps = [-1] * 128
        mapt = [-1] * 128
        sub = ord('a')
        
        for i in range(n):
            key1 = ord(s[i]) - sub
            key2 = ord(t[i]) - sub

            if maps[key1] != -1 and maps[key1] != key2:
                return False
            elif mapt[key2] != -1 and mapt[key2] != key1:
                return False
            else:
                maps[key1] = key2
                mapt[key2] = key1
        
        return True
        # maps = {}
        # mapt = {}

        # for i in range(n):
        #     key1 = s[i]
        #     key2 = t[i]
            
        #     if key1 in maps and maps[key1] != key2:
        #         return False
        #     elif key2 in mapt and mapt[key2] != key1:
        #         return False
        #     else:
        #         maps[key1] = key2
        #         mapt[key2] = key1
            
        # return True