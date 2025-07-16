class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        charDeleted = False

        start = 0
        end = len(s) - 1
        while start < end:
            if s[start] != s[end]:
                return (
                    self.validPalidrome(s, start+1, end) or
                    self.validPalidrome(s, start, end - 1))
            
            start += 1
            end -= 1

        return True
    

    def validPalidrome(self, s: str, start: int, end: int):
        
        while start < end:
            if s[start] != s[end]:
                return False
            
            start += 1
            end -= 1

        return True
        