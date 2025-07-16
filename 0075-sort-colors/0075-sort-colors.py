class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        zeroIdx = 0
        twoIdx = len(nums) -1
        oneIdx = 0

        while oneIdx <= twoIdx:
            num = nums[oneIdx]

            if num == 0:
                nums[oneIdx] = nums[zeroIdx]
                nums[zeroIdx] = 0
                zeroIdx += 1
                oneIdx += 1

            elif num == 1:
                oneIdx += 1

            else:
                nums[oneIdx] = nums[twoIdx]
                nums[twoIdx] = 2
                twoIdx -= 1


        