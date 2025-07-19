class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        no_col = len(grid[0]) #3
        no_row = len(grid)#2
        i=0 #represents rows
        j=no_col - 1 #represents columns
        total=0
        while i < no_row and j >= 0:
            if grid[i][j] < 0:  #first iteration=grid[0][3]
                total += no_row - i
                j -= 1
            else:
                i += 1
        return total            