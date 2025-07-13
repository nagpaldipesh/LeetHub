class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        result = [-1] * n

        greatestElement = arr[n-1]

        for i in range(n-2, -1, -1):
            result[i] = greatestElement

            if arr[i] > greatestElement:
                greatestElement = arr[i]
            
        
        return result
