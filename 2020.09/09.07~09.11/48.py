# matrix = [[1,2,3],[4,5,6],[7,8,9]]

def rotate(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)
    tmp = list(matrix)
    
    for i in range(n):
        matrix[i] = []
        
    for i in range(n-1, -1, -1):
        for j in range(0,n):
            matrix[j].append(tmp[i][j])