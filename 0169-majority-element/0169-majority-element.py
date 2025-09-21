class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        count = 1

        for index in range(1, len(nums)):
            if candidate == nums[index]:
                count += 1
            else:
                count -= 1

            if count <= 0:
                candidate = nums[index]
                count = 1
            

        return candidate