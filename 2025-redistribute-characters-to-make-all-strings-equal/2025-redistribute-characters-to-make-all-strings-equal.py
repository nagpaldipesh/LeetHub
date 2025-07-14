class Solution:
    def makeEqual(self, words: List[str]) -> bool:

        from collections import Counter

        freq = Counter("".join(words))
        n = len(words)

        for count in freq.values():
            if count % n != 0:
                return False
        
        return True
        # count = [0] * 26
        # hash = ord('a')

        # for word in words:
        #     for c in word:
        #         index = ord(c) - hash
        #         count[index] += 1
        
        # n = len(words)
        # for num in count:
        #     if num % n != 0:
        #         return False

        # return True
