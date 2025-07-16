class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)

        vowelCount = [0] * (n + 1)

        vowels = 'aeiou'

        for i, word in enumerate(words):
            increment = 0
            if word[0] in vowels and word[-1] in vowels:
                increment = 1

            vowelCount[i+1] = vowelCount[i] + increment

        result = []

        for l, r in queries:
            result.append(
                vowelCount[r + 1] - vowelCount[l]
            )

        return result
