#Write a Python program to check if 2 is divisble by 2 and print ("2 is divisible by 2")
number = 2

if number % 2 == 0:
    print("2 is divisible by 2")

#Wtite a Python program to check if a variable is divisible by 2
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is divisible by 2")
else:
    print(f"{number} is not divisible by 2")

#Write a Python program to find the sum of n natural numbers
n = int(input("Enter a positive integer: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    sum_of_numbers = (n * (n + 1)) // 2
    print("The sum of the first", n, "natural numbers is:", sum_of_numbers)

#Write a Python program to find the sum of the even natural numbers with the gievn range n
n = int(input("Enter a positive integer: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    sum_of_even_numbers = 0
    for num in range(2, n+1, 2):
        sum_of_even_numbers += num

    print("The sum of even natural numbers up to", n, "is:", sum_of_even_numbers)

