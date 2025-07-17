class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()

        result = ""
        for word in words:
            result = result + str(word[::-1]) + " "

        return result[0:-1]