class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False
            
        map_s = {}
        map_t = {}

        for i in range(len(pattern)):
            c = pattern[i]
            word = words[i]

            if c in map_s and map_s[c] != word:
                return False
            if word in map_t and map_t[word] != c:
                return False

            map_s[c] = word
            map_t[word] = c
        
        return True