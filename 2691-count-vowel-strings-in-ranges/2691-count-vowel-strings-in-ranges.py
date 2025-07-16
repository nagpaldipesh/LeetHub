class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)

        vowelCount = [0] * n

        vowels = 'aeiou'

        for i, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                count = 1 if i == 0 else vowelCount[i -1] + 1
                vowelCount[i] = count
            elif i > 0:
                vowelCount[i] = vowelCount[i -1]

        result = []

        for query in queries:
            count = 0
            
            if query[0] == 0:
                count = vowelCount[query[1]]
            else:
                count = vowelCount[query[1]] - vowelCount[query[0] - 1]
            result.append(count)

        return result
