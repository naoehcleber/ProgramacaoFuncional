def fibonacci(n):
    fib = lambda n: 0 if n <= 0 else (1 if n == 1 else fib(n - 1) + fib(n - 2))
    resultado = list(map(fib, (range(n))))
    return resultado

print(fibonacci(10))
