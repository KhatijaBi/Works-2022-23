def func1(arr):
    total = 0
    for num in arr:
        if num > 2:
            total += num
    return total

arr = [1, 2, 3, 4, 5, 6]
print(func1(arr))


def func2(arr):
    for i in range(len(arr)):
        if arr[i] == 2:
            arr[i] = 0

arr = [2, 2, 3, 4, 5]
func2(arr)
print(arr)


def func3(n):
    even_numbers = []
    for i in range(0, n+1, 2):
        even_numbers.append(i + 1)
    return even_numbers

print(func3(8))
