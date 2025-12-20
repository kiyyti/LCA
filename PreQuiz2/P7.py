def factorial(n):
    total = 1
    for i in range(n + 1):
        if i == 0:
            continue
        total *= i
    return total

def taylor_sin0(x, k):
    result = 0
    for i in range(k + 1):
        if i % 4 == 1:    
            result += (x**i) / factorial(i)
        elif i % 4 == 3:  
            result -= (x**i) / factorial(i)
    return result

def taylor_cos0(x, k):
    result = 0
    for i in range(k + 1):
        if i % 4 == 0:    
            result += (x**i) / factorial(i)
        elif i % 4 == 2:  
            result -= (x**i) / factorial(i)
    return result

def taylor_sin_halfpi(x, k):
    result = 0
    pi_half = 3.141592653589793 / 2
    diff = x - pi_half
    for i in range(k + 1):
        if i % 4 == 0:
            result += (diff**i) / factorial(i)
        elif i % 4 == 2:
            result -= (diff**i) / factorial(i)
    return result