class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        result = []

        l = []
        for num in nums1:
            if num not in nums2 and num not in l:
                l.append(num)

        result.append(l)

        l2 = []
        for num in nums2:
            if num not in nums1 and num not in l2:
                l2.append(num)
        
        result.append(l2)

        return result
        