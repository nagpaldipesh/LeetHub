class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()

        n = len(words)
        for i in range (n):
            word = words[i]
            #print(f"n: {n} i: {i} {i+1%n}")
            if word[-1] != words[(i+1) % n][0]:
                return False

        return True