def matdot(x, y):
    rowX = len(x)
    colX = len(x[0])
    rowY = len(y)
    colY = len(y[0])

    if colX != rowY:
        return None
    
    result = [[0 for _ in range(colY)] for _ in range(rowX)]

    for i in range(rowX):
        for j in range(colY):
            for k in range(colX):
                result[i][j] += x[i][k] * y[k][j]
    
    return result

