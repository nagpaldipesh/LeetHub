class Solution:
    def specialArray(self, nums: List[int]) -> int:
        max_num = max(nums)

        for i in range(max_num + 1):
            equalOrGreater = 0
            for num in nums:
                if num >= i:
                    equalOrGreater += 1

            if i == equalOrGreater:
                return i
            
        return -1

        return -1