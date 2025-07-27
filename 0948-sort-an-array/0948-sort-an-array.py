class Solution:
    ################### Quick SORT #######################
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quick_sort_3_ways(nums, 0, len(nums) - 1)
        return nums
    
    def quick_sort_3_ways(self, nums:List[int], low: int, high: int):

        if low >= high:
            return
        
        pivot_index = random.randint(low, high)
        nums[pivot_index], nums[low] = nums[low], nums[pivot_index]
        pivot = nums[low]

        lt, gt, i = low, high, low + 1

        while i <= gt:
            if nums[i] < pivot:
                nums[lt], nums[i] = nums[i], nums[lt]
                i += 1
                lt += 1
            
            elif nums[i] > pivot:
                nums[gt], nums[i] = nums[i], nums[gt]
                gt -= 1
            else:
                i += 1

        self.quick_sort_3_ways(nums, low, lt - 1)
        self.quick_sort_3_ways(nums, gt + 1, high)


    ################################## Time Limit Exceed #########################
    # def sortArray(self, nums: List[int]) -> List[int]:
    #     self._quick_sort(nums, 0, len(nums) - 1)

    #     return nums

    # def _quick_sort(self, nums: List[int], low: int, high:int) -> List[int]:
    #     if low < high:
    #         partition_index = self._partition(nums, low, high)

    #         self._quick_sort(nums, low, partition_index - 1)
    #         self._quick_sort(nums, partition_index + 1, high)

    # def _partition(self, nums: List[int], low: int, high: int) -> int:
    #     random_pivot_index = random.randint(low, high)
    #     nums[random_pivot_index], nums[high] = nums[high], nums[random_pivot_index] 

    #     pivot = nums[high]
    #     if low < high:
    #         i = low - 1
    #         for j in range(low, high):
    #             if nums[j] <= pivot:
    #                 i += 1
    #                 nums[i], nums[j] = nums[j], nums[i]

    #         nums[i +1], nums[high] = nums[high], nums[i+1]

    #     return i + 1


    ###################### MERGE SORT ##################### 
    # def sortArray(self, nums: List[int]) -> List[int]:
    #     n = len(nums)
    #     if n <= 1:
    #         return nums

    #     mid = n // 2 

    #     left_half = self.sortArray(nums[:mid])
    #     right_half = self.sortArray(nums[mid:])

    #     return self.merge(left_half, right_half)

    # def merge(self, left: List[int], right: List[int]) -> List[int]:
    #     sorted_list = []

    #     i = j = 0

    #     while i < len(left) and j < len(right):
    #         if left[i] < right[j]:
    #             sorted_list.append(left[i])
    #             i += 1
    #         else:
    #             sorted_list.append(right[j])
    #             j += 1
            
    #     sorted_list.extend(left[i:])

    #     sorted_list.extend(right[j:])

    #     return sorted_list