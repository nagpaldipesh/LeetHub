class Solution:
    ################### Quick SORT #######################
    def sortArray(self, nums: List[int]) -> List[int]:
        self._quick_sort_3_ways(nums, 0, len(nums) - 1)
        return nums

    def _quick_sort_3_ways(self, nums: List[int], low: int, high: int):
        # --- FIX 1: Correct Base Case ---
        # The recursion should stop if the sub-array has 0 or 1 elements.
        if low >= high:
            return 
        
        # This part of choosing the pivot is fine
        pivot_index = random.randint(low, high)
        nums[low], nums[pivot_index] = nums[pivot_index], nums[low]
        pivot = nums[low]

        # lt: pointer for the end of the 'less than' section
        # gt: pointer for the start of the 'greater than' section
        # i: current element scanner
        lt, gt, i = low, high, low + 1

        # --- FIX 2: Correct Partition Logic ---
        while i <= gt:
            if nums[i] < pivot:
                # Element is smaller than pivot, move it to the 'lt' section
                nums[lt], nums[i] = nums[i], nums[lt]
                lt += 1
                i += 1
            elif nums[i] > pivot:
                # Element is larger than pivot, move it to the 'gt' section
                nums[i], nums[gt] = nums[gt], nums[i]
                gt -= 1
            else: # nums[i] == pivot
                # Element is equal, just move the scanner
                i += 1
        
        # Recursive calls on the 'less than' and 'greater than' parts
        self._quick_sort_3_ways(nums, low, lt - 1)
        self._quick_sort_3_ways(nums, gt + 1, high)
        
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