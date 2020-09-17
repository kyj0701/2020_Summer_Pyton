# matrix = []

# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         if  target == matrix[i][j]:
#             return True
# return False


if not matrix:
    return False
m = len(matrix)
n = len(matrix[0])

start = 0
end = (m * n) - 1

while (start <= end):
    mid = (start + end) // 2
    xmid = mid // n
    ymid = mid % n
    
    if target == matrix[xmid][ymid]:
        return True
    elif target > matrix[xmid][ymid]:
        start = mid + 1
    else:
        end = mid - 1
        
return False