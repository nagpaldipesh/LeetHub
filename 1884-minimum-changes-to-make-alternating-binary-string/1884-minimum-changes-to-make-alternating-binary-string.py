class Solution:
    def minOperations(self, s: str) -> int:
        
        count = count1 = 0

        for i, c in enumerate(s):
            #expected_1 = '0' if i % 2 == 0 else '1'
            #expected_2 = '1' if i % 2 == 0 else '0'

            if c != str(i % 2): 
                count += 1
            if c != str((i +1) % 2): 
                count1 += 1
        
        return min(count, count1)