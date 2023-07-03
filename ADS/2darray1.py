#1
grid = [
    [8,2,7,5,3,6,9,4,1],
    [5,1,6,8,4,9,3,2,7],
    [9,4,3,1,7,2,6,5,8],
    [2,7,1,3,9,4,8,6,5],
    [3,6,5,7,1,8,2,9,4],
    [4,9,8,6,2,5,1,7,3],
    [6,5,2,4,8,3,7,1,9],
    [1,8,9,2,5,7,4,3,6],
    [7,3,4,9,6,1,5,8,2]
]
print(grid)

#2
row = 1
def check_row(grid,row_no,elem):
   for column in range(9):
      if grid[row_no][column] == elem:
        return True
   return False
print(check_row(grid,3,4))

#2
column = 1
def check_column(grid,column_no,elem):
    for row in range(9):
       if grid[column_no][row] == elem:
         return True
    return False
print(check_column(grid,3,4))

#3 box

#4 #Create a function which will print the elements of the diagonals of the 9x9 grid(Parameters: Grid)
grid = [
    [1, 3, 5, 8, 2, 4, 6, 7, 9],
    [2, 1, 3, 4, 5, 7, 8, 9, 6],
    [3, 2, 4, 5, 9, 8, 7, 1, 5],
    [4, 5, 1, 2, 1, 6, 7,8, 9],
    [5, 4, 2, 1, 3, 7, 8, 4, 5],
    [6, 7, 9, 3, 6, 8, 9, 3, 2],
    [7, 6, 8, 6, 7, 4, 5, 2, 1],
    [8, 9, 6, 7, 4, 1, 2, 3, 8],
    [9, 4, 7, 9, 8, 5, 3, 1, 2]
]
def diagonals(grid):
    for i in range(9):
        print(grid[i][i],end=" ")
    print("\n")
    for i in range(9):
        print(grid[i][8-i],end=' ')
diagonals(grid)