class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sl = []

        for c in s:
            if c != '#':
                sl.append(c)
            elif len(sl) > 0:
                sl.pop() 

        st = []
        for c in t:
            if c != '#':
                st.append(c)
            elif len(st) > 0:
                st.pop() 

        return st == sl
        