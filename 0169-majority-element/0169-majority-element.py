class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = -1
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
                count = 1
                continue
            
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate
