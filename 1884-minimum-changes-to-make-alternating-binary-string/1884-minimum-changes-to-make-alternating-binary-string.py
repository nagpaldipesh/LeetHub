class Solution:
    def minOperations(self, s: str) -> int:
        
        count = count1 = 0

        for i in range(len(s)):
            expected_1 = '0' if i % 2 == 0 else '1'
            expected_2 = '1' if i % 2 == 0 else '0'

            if s[i] != expected_1: 
                count += 1
            elif s[i] != expected_2: 
                count1 += 1
        
        return min(count, count1)