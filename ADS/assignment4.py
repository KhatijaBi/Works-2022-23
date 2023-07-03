#python code for sum of even numbers onwards 2 using for loop
n = int(input("Enter a number: "))
sum = 0
for i in range(2, n+1, 2):
    sum += i
print(sum)
sum = 0
for i in range(1, n+1, 2):
    sum += i
print(sum)


