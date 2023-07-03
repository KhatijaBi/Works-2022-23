#Define a function to find the sum of n natural numbers using a loop
def sum_natural_for_loop(n):
     sum = 0
     for i in range(n+1):
         sum = i + sum
     return sum
print(sum_natural_for_loop(5))


#Define a function to find the sum of n natural numbers using recursion
def sum_natural_recursion(n):
    if n == 1:
        return 1
    else:
        return n + sum_natural_recursion(n-1)
print(sum_natural_recursion(10))

#Define a function to find the factorial of a number using recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n - 1) * n
print(factorial(10))

#Define a function to find the nth number in the fibonacci series using recursion(optional)
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(6))