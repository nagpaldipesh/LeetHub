class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        lastChar = 't'

        for c in s:
            if c != ' ' and lastChar == ' ':
                length = 0
            
            if c != ' ':
                length += 1
            
            lastChar = c
        
        return length
        # word = ""
        # lastChar = 't'

        # for c in s:
        #     if lastChar == ' ' and c != ' ':
        #         word = ""
            
        #     if c != ' ':
        #         word += c
            
        #     lastChar = c
        
        # return len(word)