def factorial(n):
    sum = 1
    for i in range(n+1):
        if i == 0:
            continue
        sum *= i
    return sum

