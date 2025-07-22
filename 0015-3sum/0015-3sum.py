class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        results = []
        nums.sort()
        n = len(nums)

        for i in range(n):
            num = nums[i]
            
            if i > 0 and num == nums[i - 1]:
                continue

            if num > 0:
                break

            left = i+1
            right = n -1

            while left < right:
                sum = num + nums[left] + nums[right]

                if sum == 0:
                    results.append([num, nums[left], nums[right]])
                
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                
                elif sum > 0:
                    right -= 1
                else:
                    left += 1

        return results