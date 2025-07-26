class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        max_product = min_product = result = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            candidates = (num, num * max_product, num * min_product)
            max_product , min_product = max(candidates), min(candidates)
            
            result = max(result, max_product)

        return result