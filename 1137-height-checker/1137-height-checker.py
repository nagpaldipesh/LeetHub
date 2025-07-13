class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        import copy
        expected = copy.copy(heights)
        expected.sort()

        incorrect = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                incorrect += 1
        
        return incorrect