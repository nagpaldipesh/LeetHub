class Solution:
    def specialArray(self, nums: List[int]) -> int:
        # nums.sort()
        # n = len(nums)

        # for i in range(1, nums[n-1] + 1):

        max_num = max(nums)

        for i in range(1, len(nums) + 1):
            equalOrGreater = 0
            for num in nums:
                if num >= i:
                    equalOrGreater += 1

            if i == equalOrGreater:
                return i
            
        return -1

    # def get_lower_bount(self, num: List[int], n : int) -> int:
    #     low = 0
    #     high = n

    #     idx = n
        
    #     while low <= high:
    #         mid = low + (high - low) /2

    #         if ()