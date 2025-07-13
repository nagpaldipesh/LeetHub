class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        placed_flowers = 0
        count = len(flowerbed)
        for i in range(count):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == count -1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                placed_flowers += 1 
            
            # print(placed_flowers)
            if placed_flowers == n:
                return True
        
        # print(placed_flowers)    
        return placed_flowers >= n