class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = ""
        lastChar = 't'

        for c in s:
            if lastChar == ' ' and c != ' ':
                word = ""
            
            if c != ' ':
                word += c
            
            lastChar = c
        
        return len(word)