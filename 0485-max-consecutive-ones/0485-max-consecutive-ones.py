class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        maxOnesCount = 0
        onesSoFar = 0

        for num in nums:

            if num == 1:
                onesSoFar += 1
            
                maxOnesCount = max(maxOnesCount, onesSoFar)

            else:
                onesSoFar = 0

        
        return maxOnesCount