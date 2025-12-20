def gauss_jordan(a, b):
    n = len(a)
    aug = []
    for i in range(n):
        aug.append(a[i] + b[i])

    for i in range(n):
        pivot = aug[i][i]
        
        for j in range(len(aug[i])):
            aug[i][j] = aug[i][j] / pivot
            
        for r in range(n):
            if r != i:  
                factor = aug[r][i]
                for j in range(len(aug[i])):
                    aug[r][j] = aug[r][j] - (factor * aug[i][j])
    
    x = [[row[-1]] for row in aug]
    return x

