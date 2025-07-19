class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        productFromRight = [1] * (n+1)
        result = []

        for i in reversed(range(n)):
            productFromRight[i] = productFromRight[i + 1] * nums[i]

        product = 1
        for i in range(n):
            result.append(product * productFromRight[i+1])
            product *= nums[i]

        return result