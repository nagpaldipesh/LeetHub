class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicateNumber = -1

        for num in nums:
            index = abs(num) - 1

            if nums[index] < 1:
                duplicateNumber = index + 1
            else:
                nums[index] *= -1 

        for i, num in enumerate(nums):
            if num > 0:
                return [duplicateNumber, i + 1]

        return [-1, -1]