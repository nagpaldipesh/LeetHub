class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numIndex = {}

        for index, num in enumerate(nums):

            numToCheck = target - num

            if numToCheck in numIndex:
                return [numIndex[numToCheck], index]
            
            else:

                numIndex[num] = index
            
        return (-1, -1)