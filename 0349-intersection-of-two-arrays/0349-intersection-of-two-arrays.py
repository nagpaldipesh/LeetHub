class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = [0] * 1001

        for num in nums1:
            count[num] = 1
        
        result = []

        for num in nums2:
            if count[num] == 1:
              result.append(num)  
              count[num] = 0

        return result