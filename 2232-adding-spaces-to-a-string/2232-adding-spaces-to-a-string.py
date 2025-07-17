class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        
        words = []
        index = 0
        for i in range(len(spaces)):
            words.append(s[index:spaces[i]])
            index = spaces[i]
            #print(index)

        words.append(s[index:])

        return " ".join(words)