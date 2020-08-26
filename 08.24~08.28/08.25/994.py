# grid = [[2,1,1],[1,1,0],[0,1,1]]

def orangesRotting(self, grid: List[List[int]]) -> int:
    q = []
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 2:
                q.append([i,j])
    ans = -1
    while q:
        tmp = []
        while q:
            tmp.append(q.pop(0))
        for pair in tmp:
            if pair[0]-1 >= 0 and grid[pair[0]-1][pair[1]] == 1:
                grid[pair[0]-1][pair[1]] = 2
                q.append([pair[0]-1,pair[1]])
            if pair[1]-1 >= 0 and grid[pair[0]][pair[1]-1] == 1:
                grid[pair[0]][pair[1]-1] = 2
                q.append([pair[0],pair[1]-1])
            if pair[0]+1 < len(grid) and grid[pair[0]+1][pair[1]] == 1:
                grid[pair[0]+1][pair[1]] = 2
                q.append([pair[0]+1,pair[1]])
            if pair[1]+1 < len(grid[0]) and grid[pair[0]][pair[1]+1] == 1:
                grid[pair[0]][pair[1]+1] = 2
                q.append([pair[0],pair[1]+1])
        ans += 1
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                return -1
    
    if ans == -1:
        return 0
    else:
        return ans