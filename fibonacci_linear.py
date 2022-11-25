def fibonacci(n):
    first = 0
    second = 1
    total = 0
    if n<2:
        total = n
    for x in range(1, n):
        total = first + second
        first = second
        second = total
    return total

n = int(input('Pick a number\n'))
print(fibonacci(n))