class Solution:
    def minOperations(self, logs: List[str]) -> int:
        hierarcy_level = 0

        for log in logs:
            if '../' in log:
                if hierarcy_level > 0:
                    hierarcy_level -= 1
            elif './' in log:
                continue
            else:
                hierarcy_level += 1
            
        
        return hierarcy_level
            