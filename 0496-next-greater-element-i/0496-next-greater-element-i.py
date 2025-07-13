class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        map = {}

        for num in reversed(nums2):
            while(len(stack) > 0 and stack[-1] < num):
                stack.pop()

            map[num] = stack[-1] if len(stack) > 0 else -1
            stack.append(num)

        result = []

        for num in nums1:
            result.append(map[num])

        return result
