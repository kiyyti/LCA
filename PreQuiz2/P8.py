def factorial(n):
    total = 1
    for i in range(n + 1):
        if i == 0: continue
        total *= i
    return total

def taylor_exp0(x, k):
    result = 0.0
    for i in range(k + 1):
        term = (x**i) / factorial(i)
        result += term
    return result

