#Write a Python function to check if a given number is odd or even
def even_or_odd(n):
    if n % 2 == 0:
        print ("even")
    else:
        print("odd")
even_or_odd(2)

#Write a Python function to print all the elements in a given range
def print_range(start,end):
    for n in range(start, end+1):
        print(n)
print_range(1, 10)

#Write a Python function to find the factorial of a number using recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(6))  

#Write a Python function to check if a number is there:
#1.in a given 3*3 box(Parameters, Grid, row_no, column_no, element)

grid=[
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [4, 5, 6, 5, 6, 7, 8, 9, 1],
    [7, 8, 9, 6, 7, 8, 9, 1, 2],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [5, 6, 7, 8, 9, 1, 2, 3, 4],
    [6, 7, 8, 9, 1, 2, 3, 4, 5],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [8, 9, 1, 2, 3, 4, 5, 6, 7],
    [9, 1, 2, 3, 4, 5, 6, 7, 8]
]

def check_box(grid, row_no, column_no, element):
    box_row = (row_no // 3) * 3
    box_col = (column_no // 3) * 3
    for r in range(box_row, box_row + 3):
        for c in range(box_col, box_col + 3):
            if grid[r][c] == element:
                return True
    return False
print(check_box(grid, 1, 2, 9))