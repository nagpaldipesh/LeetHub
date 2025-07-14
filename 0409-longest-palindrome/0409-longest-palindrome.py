class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter

        freq = Counter(s)

        longestPalindromeCount = 0
        oneToCount = True

        for count in freq.values():
            longestPalindromeCount += (2 * int(count / 2))

            if oneToCount and (count % 2 == 1):
                longestPalindromeCount += 1
                oneToCount = False
        
        return longestPalindromeCount

