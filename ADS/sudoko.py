#Check a box given the row and column of top-left element for an element(Parameters: grid, box_row, box_column, element)
grid1 = [
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

grid2 = [
    [1,2,3,4,5,6,7,8,9], 
    [2,3,4,5,6,7,8,9,1], 
    [3,4,5,6,7,8,9,1,2], 
    [4,5,6,7,8,9,1,2,3], 
    [5,6,7,8,9,1,2,3,4], 
    [6,7,8,9,1,2,3,4,5], 
    [7,8,9,1,2,3,4,5,6], 
    [8,9,1,2,3,4,5,6,7], 
    [9,1,2,3,4,5,6,7,8]
]

grid3 = [
[5,3,2,1,4,6,7,8,5], 
[1,4,6,7,8,9,2,5,3], 
[7,8,9,2,5,3,1,4,6], 
[2,1,3,4,6,5,8,9,7], 
[4,5,7,8,9,1,3,6,2], 
[6,9,8,3,2,7,4,1,5],
[3,2,5,6,1,4,9,7,8], 
[8,6,1,9,7,2,5,3,4], 
[9,7,4,5,3,8,6,2,1]
]


#Check a column for all the numbers from 1-9  (Parameters: grid, column_no)
def check_column(grid,column_no,elem):
    for row in range(9):
       if grid[column_no][row] == elem:
         return True
    return False
#print(check_column(grid,3,4))

#Check a given row for all the numbers from 1-9(Parameters: grid, row_no)
def check_row(grid,row_no,elem):
   for column in range(9):
      if grid[row_no][column]== elem:
        return True
   return False

def check_all_rows(grid,row_no):
    for i in range(1,10):
      if(check_row(grid,row_no,i))==False:
         return False
    #return True

#Check a column for all the numbers from 1-9  (Parameters: grid, column_no)
def check_all_columns(grid,row_no):
    for i in range(1,10):
       if(check_column(grid,row_no,i))==False:
          return False
    return True

#Check a box for all the numbers from 1-9  (Parameters: grid, box_row, box_column)
def check_box(grid,box_row,box_column,elem):
   for r in range(box_row,box_row+3):
      for c in range(box_column,box_column+3):
         if(grid[r][c] == elem):
            return True
   return False

def check_all_boxes(grid,box_row,column_row):
   for i in range(1,10):
      if(check_box(grid,box_row,column_row,i))== False:
        return False
   return True

#Write a check grid functions which will check all the rows, columns and boxes for all the numbers from 1-9
def check_grid(grid):
# Check all rows
    for r in range(9):
       if (check_all_rows(grid, r))==False:
          return False
       
# Check all columns
    for c in range(9):
       if (check_all_columns(grid, c))==False:
          return False
   
# Check all boxes
    for box_r in range(0, 9, 3):
        for box_c in range(0, 9, 3):
            if (check_all_boxes(grid, box_r, box_c))==False:
                return False
    return True
def check_all_grids(grid):
 if(check_grid(grid) == True):
    print("CORRECT")
 else:
   print("INCORRECT")

check_all_grids(grid1)
check_all_grids(grid2)
check_all_grids(grid3)

