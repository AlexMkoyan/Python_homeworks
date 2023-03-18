def fib(n):
    fibs = [0,1]
    for i in range(2, n+1):
        fibs.append(fibs[i-1] + fibs[i-2])
    return fibs

print(fib(2))
print(fib(3))
print(fib(7))

def fib_rec(n):
    if n == 0:
        return(0)
    if n == 1:
        return(1)

    return(fib_rec(n-1) + fib_rec(n-2))
print(fib_rec(7))