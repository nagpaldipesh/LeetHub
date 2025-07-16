class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        squares = [num* num for num in nums]
        # for i in range(len(nums)):
        #     nums[i] *= nums[i]

        squares.sort()
        return squares
