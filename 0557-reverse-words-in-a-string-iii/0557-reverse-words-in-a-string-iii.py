class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()

        reversed_words = [word[::-1] for word in words]

        return " ".join(reversed_words)
        # words = s.split()

        # result = ""
        # for word in words:
        #     result = result + str(word[::-1]) + " "

        # return result[0:-1]