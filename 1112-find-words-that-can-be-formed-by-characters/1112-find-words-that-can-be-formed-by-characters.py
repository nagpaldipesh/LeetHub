class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        from collections import Counter

        freq = Counter(chars)
        count = 0

        for word in words:
            freq2 = Counter(word)

            is_good = True
            for (k, v) in freq2.items():
                if not k in freq or freq[k] < v:
                    is_good = False
                    break
            
            if is_good:
                count += len(word)

        return count