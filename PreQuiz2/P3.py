def determinant(x):
    n = len(x)

    if n == 1:
        return x[0][0]

    if n == 2:
        return (x[0][0] * x[1][1]) - (x[0][1] * x[1][0])

    det = 0
    for j in range(n):
        minor = [row[:j] + row[j+1:] for row in x[1:]]
        sign = (-1) ** j
        det += sign * x[0][j] * determinant(minor)
        
    return det

