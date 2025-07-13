class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest = strs[0]

        for s in strs:
            if len(smallest) < len(s):
                smallest = s

        n = len(smallest)
        index = n-1

        for i in range(len(strs)):
            while index >= 0:
                if strs[i].startswith(smallest):
                    break
                else:
                    smallest = smallest[0:index]
                    index -= 1
            
        return smallest

