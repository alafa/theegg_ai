#https://www.youtube.com/watch?v=DiAtV7SneRE

# Simple recursive program for Fibonacci numbers

def fib(n):

    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


print(fib(4))