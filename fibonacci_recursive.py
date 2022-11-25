

def fibonacci(n):
    if n <= 1:
        return(n)
    elif n <= 30:
        return(fibonacci(n-1)+fibonacci(n-2))
    elif n <0 or n > 30:
        return('Number not included in this program.')

n = int(input('Pick a number\n'))
print(fibonacci(n))