def fibonacci(n):
    return n if n < 2 else fibonacci(n-2) + fibonacci(n-1)

for n in range(1, 11):
    print(n, ":", fibonacci(n))
