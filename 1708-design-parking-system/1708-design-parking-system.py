class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

        # self.slots = {
        #     1: big,
        #     2: medium,
        #     3: small
        # }

    def addCar(self, carType: int) -> bool:
        # if(self.slots[carType] > 0):
        #     self.slots[carType] -= 1
        #     return True
        
        match carType:
            case 1:
                if self.big > 0:
                    self.big -= 1
                    return True
            case 2:
                if self.medium > 0:
                    self.medium -= 1
                    return True
            case 3:
                if self.small > 0:
                    self.small -= 1
                    return True

        return False
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)