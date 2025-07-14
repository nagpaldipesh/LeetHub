class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        timeRequired = 0
        
        for i in range(len(tickets)):

            if i <= k:
                timeRequired += min(tickets[k], tickets[i])
            else:
                timeRequired += min(tickets[i], tickets[k] - 1)

        return timeRequired