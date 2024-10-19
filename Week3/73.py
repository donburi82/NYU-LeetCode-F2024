# 73. Set Matrix Zeroes
# O(mn) space solution by having a matrix copy - repeated work
# O(m+n) space, O(mn) time solution by marking which row/column to fill zeroes with
# O(1) space, O(mn) time solution by using the first row+column and a single variable as marker
def setZeroes(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    m, n = len(matrix), len(matrix[0])
    firstRowZero = False
    
    # mark which row/column to fill zeroes with
    for i in range(m):
        for j in range(n):
            if matrix[i][j]==0:
                matrix[0][j] = 0 # need to fill this column with zeros
                if i>0:
                    matrix[i][0] = 0 # need to fill this row with zeros
                else:
                    firstRowZero = True

    # handle non-marking positions first
    for i in range(1, m):
        for j in range(1, n):
            if matrix[0][j]==0 or matrix[i][0]==0:
                matrix[i][j] = 0

    # handle marking positions
    if matrix[0][0]==0:
        for i in range(m):
            matrix[i][0] = 0

    if firstRowZero:
        for j in range(n):
            matrix[0][j] = 0        
