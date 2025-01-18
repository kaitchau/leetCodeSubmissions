class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter=0
        #row
        for i in range(len(grid)):
            #column
            for j in range(len(grid[i])):
                if grid[i][j]==1:
                    #it's land, check all sides for perimeter
                    #left
                    if j==0 or grid[i][j-1]==0:
                        perimeter+=1
                    #right
                    if j==len(grid[i])-1 or grid[i][j+1]==0:
                        perimeter+=1
                    #up
                    if i==0 or grid[i-1][j]==0:
                        perimeter+=1
                    #down
                    if i==len(grid)-1 or grid[i+1][j]==0:
                        perimeter+=1
        return perimeter

        