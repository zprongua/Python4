def factorial():
    n = int(input('Tell me the number you want the factorial of:\n'))
    if n <= 0 or n >995:
        print('Number out of range for this program.')
    total = 1
    for x in range(1, n+1):
        total = total * x
    print(total)

factorial()