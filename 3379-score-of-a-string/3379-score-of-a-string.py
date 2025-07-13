class Solution:
    def scoreOfString(self, s: str) -> int:
        maxScore = 0

        for i in range(len(s) -1):
            maxScore = maxScore + abs(ord(s[i]) - ord(s[i+1]))

        return maxScore