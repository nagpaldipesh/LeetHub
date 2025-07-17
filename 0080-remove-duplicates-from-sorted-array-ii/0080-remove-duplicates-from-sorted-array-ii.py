class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        count = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                count += 1
            else:
                if count > 2:
                    count = 2
                
                for j in range(count):
                    nums[index] = nums[i-1]
                    index += 1
                    
                count = 1
        
        if count > 2:
            count = 2
                
        for i in range(count):
            nums[index] = nums[-1]
            index += 1
            
        return index
