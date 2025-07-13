class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        
        import sys

        largest = secondlargest = -1 
        smallest = secondsmallest = sys.maxsize

        for num in nums:
            if num > largest:
                secondlargest = largest
                largest = num
            elif num > secondlargest:
                secondlargest = num
            
            if num < smallest:
                secondsmallest = smallest
                smallest = num
            elif num < secondsmallest:
                secondsmallest = num
        
        return (largest * secondlargest) - (smallest * secondsmallest)