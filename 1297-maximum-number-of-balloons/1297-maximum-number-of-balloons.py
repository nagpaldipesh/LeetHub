class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        from collections import Counter
        freq = Counter(text)

        counts = {
            'b' : 1,
            'a' : 1,
            'l' : 2,
            'o' : 2,
            'n' : 1
        }

        import sys
        total_ballons = sys.maxsize
        for key in counts:
            
            #print(f"Key: {key}  Freq: {freq[key]} Count: {counts[key]} C: {freq[key] if key in freq else 0 / counts[key]}")
            total_ballons = min(total_ballons, 
            freq[key] // counts[key] if key in freq else 0)

        return int(total_ballons)