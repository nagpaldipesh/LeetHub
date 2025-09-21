class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k = k % len(nums) 

        def rotate(nums: List[int], start:int, end: int) -> None:
            
            #print(end)
            while start < end:
                nums[end] , nums[start] = nums[start] , nums[end]

                start += 1
                end -= 1
            
        end= len(nums) - 1

        rotate(nums, 0, end)
        rotate(nums, 0, k-1)
        rotate(nums, k, end)