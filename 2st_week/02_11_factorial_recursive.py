# 3! = 3 * 2 * 1

# factorial(n) = n* factorial(n-1)
# factorial(n - 1) = (n-1) * factorial(n-2)

# factorial(1) = 1

def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)

# 5*4*3*2*1 = 120
print(factorial(5))
