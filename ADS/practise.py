#Write a Python program to find if a given number is even or odd:
def even_or_odd(n):
    if n % 2 == 0:
        print ("Even")
    else:
        print("Odd")
print (even_or_odd(5))
print (even_or_odd(6))

#Write a Python program to find the largest of the three given numbers:
def largest_of_three(a,b,c):
    largest = a
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    return largest
print(largest_of_three(40, 10, 30))
print(largest_of_three(60, 50, 40))

#Write a Python program to check if a given number is prime:
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(is_prime(5)) 
print(is_prime(10)) 

#Write a Python program to check if a given number is positive or negative:
def positive_or_negative(n):
    if n >= 0:
        print("Positive")
    else:
        print("Negative")
positive_or_negative(10) 
positive_or_negative(-5)

#Loop
#Write a Python program to print all the numbers within a given range:
def print_range(start, end):
    for n in range(start, end+1):
        print(n)
print_range(1, 10)

#Write a Python program to find the sum of all even numbers within a given range:
def sum_of_evens(start, end):
    total = 0
    for n in range(start, end+1):
        if n % 2 == 0:
            total += n
    return total
print(sum_of_evens(1, 10))

#Write a Python program to find the factorial of a number using a loop:
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
print(factorial(5))

#Write a Python program to find the nth fibonacci number using a loop
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n+1):
            c = a + b
            a, b = b, c
        return b

print(fibonacci(7)) 


#Write a Python program to find the largest number in a list:
def largest_number(numbers):
    largest = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest

numbers = [1, 5, 9, 2, 7]
print(largest_number(numbers)) 

#Recursion:
#Write a Python program to find the factorial of a number using recursion
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)

print(factorial(5))

#Write a Python program to find the power of a number using recursion given base and exponent
def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp-1)

print(power(2, 3))

#Write a Python program to find the sum of all elements in a list using recursion
def sum_of_list(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return numbers[0] + sum_of_list(numbers[1:])

numbers = [1, 5, 9, 2, 7]
print(sum_of_list(numbers)) 

#Write a Python program to reverse a string using recursion
def reverse_string(string):
    if len(string) == 0:
        return ""
    else:
        return string[-1] + reverse_string(string[:-1])

string = "hello"
print(reverse_string(string))

#2D Array:

#Write a Python program to find a number :in a given row, in a given column, in a given box

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

# Find a number in a given row
def find_in_row(grid, row, number):
    if number in grid[row]:
        return True
    else:
        return False

# Find a number in a given column
def find_in_column(grid, column, number):
    for row in range(9):
        if grid[row][column] == number:
            return True
    return False

# Find a number in a given box
def find_in_box(grid, box_row, box_column, number):
    for r in range(box_row, box_row+3):
        for c in range(box_column, box_column+3):
            if grid[r][c] == number:
                return True
    return False
print(find_in_row(grid, 3, 9)) #T
print(find_in_row(grid, 5, 1)) #T
print(find_in_row(grid, 8, 5)) #F

print(find_in_column(grid, 2, 4)) #T
print(find_in_column(grid, 7, 3)) #F

print(find_in_box(grid, 0, 0, 7)) #T
print(find_in_box(grid, 3, 3, 3)) #T
print(find_in_box(grid, 6, 6, 9)) #F

