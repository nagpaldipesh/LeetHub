class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0

        left = 0
        right = len(height) -1

        while left < right:
            l = height[left]
            r = height[right]
            maxArea = max(
                maxArea,
                min(l, r) * (right - left )
            )

            if l > r:
                right -= 1
            else:
                left += 1
        
        return maxArea