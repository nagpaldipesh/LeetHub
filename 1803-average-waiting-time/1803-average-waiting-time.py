class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        if(len(customers) < 1):
            return 0

        waitingTime = 0

        end = customers[0][0]

        for customer in customers:
            if(end >= customer[0]):
                end +=  customer[-1]
            else:
                end = customer[0] + customer[-1]

            waitingTime += end - customer[0]
            
        return waitingTime / len(customers)