class Solution:
    def largestOddNumber(self, num: str) -> str:
        
        n = len(num)

        for i in reversed(range(n)):
            #print(x)
            if (int(num[i]) % 2 == 1):
                return num[0: i+1]

        return "" 