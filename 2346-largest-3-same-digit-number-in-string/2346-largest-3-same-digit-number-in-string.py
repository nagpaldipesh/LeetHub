class Solution:
    def largestGoodInteger(self, num: str) -> str:
        good_integers = ["999", "888", "777", "666", "555", "444", "333", "222", "111", "000"]
        #s = '' + num
        
        for n in good_integers:
            if n in num:
                return n

        return ""    