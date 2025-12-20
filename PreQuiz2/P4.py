def swoprow(A, x, b):
    new_matrix = list(A)
    new_matrix[x], new_matrix[b] = new_matrix[b], new_matrix[x]
    
    return new_matrix

