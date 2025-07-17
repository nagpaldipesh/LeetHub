class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        countFromRight = [0] * (n + 1) 

        for i in reversed(range(n)):
            if blocks[i] == 'B':
                countFromRight[i] = countFromRight[i+1] + 1
            else:
                countFromRight[i] = countFromRight[i+1]
        
        min_recolors = 1001 # result will always <= 100

        for i in range(0, (n - k) + 1):
            #print(countFromRight[i+k], countFromRight[i])
            min_recolors = min(
                min_recolors,
                k - (countFromRight[i] - countFromRight[i+k])
                )
        
        return min_recolors