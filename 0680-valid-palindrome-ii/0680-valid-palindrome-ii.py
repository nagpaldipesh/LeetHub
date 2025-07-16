class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        start = 0
        end = len(s) - 1
        while start < end:
            if s[start] != s[end]:
                return (
                    self.isPalindrome(s, start+1, end) or
                    self.isPalindrome(s, start, end - 1))
            
            start += 1
            end -= 1

        return True
    

    def isPalindrome(self, s: str, start: int, end: int) -> bool:
        
        while start < end:
            if s[start] != s[end]:
                return False
            
            start += 1
            end -= 1

        return True
        