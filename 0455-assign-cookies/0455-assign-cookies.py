class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        cookie_g = cookie_s = 0

        cookies = 0
        while cookie_g < len(g) and cookie_s < len(s):
            if s[cookie_s] >= g[cookie_g]:
                cookies += 1
                cookie_g += 1
            
            cookie_s += 1

        return cookies    
