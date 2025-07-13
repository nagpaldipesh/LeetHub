class Solution:
    def maxScore(self, s: str) -> int:
        ones = 0

        for c in s:
            if c == '1':
                ones += 1

        zeros = 0
        
        maxScore = 0
        for i in range(len(s) - 1):
            c = s[i]
            if c == '0':
                zeros += 1
            else :
                ones -= 1

            maxScore = max(maxScore, (ones + zeros))

        return maxScore