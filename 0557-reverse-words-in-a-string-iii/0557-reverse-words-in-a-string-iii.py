class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()

        result = ""
        for i in range(len(words)):
            result = result + str(words[i][::-1]) + " "

        return result[0:-1]