class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)

        if k > n:
            k %= n

        self.rotate_by_indexes(nums, 0, n - 1)
        self.rotate_by_indexes(nums, 0, k - 1)
        self.rotate_by_indexes(nums, k, n - 1)
        # for i in range(k):
        #     num = nums.pop()
        #     nums.insert(0, num)

    
    def rotate_by_indexes(self, nums: List[int], start: int, end: int) -> None:

        while start < end:
            nums[start] , nums [end] = nums[end], nums[start]
            start += 1
            end -= 1