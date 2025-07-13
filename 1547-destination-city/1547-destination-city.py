class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        map = {}

        for path in paths:
            map[path[0]] = path[1]

        for (k,v) in map.items():
            if v not in map:
                return v        

        return ""