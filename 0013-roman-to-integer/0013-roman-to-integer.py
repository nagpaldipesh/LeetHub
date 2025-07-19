class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        n = len(s)
        num = roman_map[s[n - 1]]
        for i in reversed(range(n -1)):
            c = s[i]
            # next_char = s[i+1]
            # if ((c == 'I' and next_char in 'VX') or (c == 'X' and next_char in 'LC') or (c == 'C' and next_char in 'DM')):
            if roman_map[c] < roman_map[s[i+1]]:
                num -= roman_map[c]
            else:
                num += roman_map[c]
        
        return num