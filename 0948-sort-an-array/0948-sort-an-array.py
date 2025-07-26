class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n <= 1:
            return nums

        mid = n // 2 

        left_half = self.sortArray(nums[:mid])
        right_half = self.sortArray(nums[mid:])

        return self.merge(left_half, right_half)

    def merge(self, left: List[int], right: List[int]) -> List[int]:
        sorted_list = []

        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_list.append(left[i])
                i += 1
            else:
                sorted_list.append(right[j])
                j += 1
            
        sorted_list.extend(left[i:])

        sorted_list.extend(right[j:])

        return sorted_list