class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_location = []

        for m in range(len(matrix)):
            for n in range(len(matrix[0])):
                if matrix[m][n] == 0:
                    zero_location.append([m, n])
        
        for m,n in zero_location:
            
            # Update row to zero
            for column in range(len(matrix[0])):
                matrix[m][column] = 0

            # Update column to zero
            for row in range(len(matrix)):
                matrix[row][n] = 0
            