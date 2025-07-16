class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # return haystack.find(needle)

        n = len(needle)
        for i in range(len(haystack) - n + 1):
            #print(haystack[i: n+1])
            if needle == haystack[i: i + n]:
                return i
        
        return -1