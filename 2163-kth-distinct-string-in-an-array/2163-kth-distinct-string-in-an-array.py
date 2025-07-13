class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        map = {}

        for s in arr:
            if s in map:
                map[s] += 1
            else:
                map[s] = 1
        
        index = 0
        for key in map:
            if map[key] == 1:
                index += 1
            
            if index == k:
                return key 

        return ""