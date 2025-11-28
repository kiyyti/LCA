import numpy as np

def add_mat(f1, f2, outf):
    matrix1 = np.loadtxt(f1, dtype=int)
    matrix2 = np.loadtxt(f2, dtype=int)

    if matrix1.shape != matrix2.shape:
        open(outf, 'w').close()
        return
    
    re_matrix = matrix1 + matrix2
    np.savetxt(outf, re_matrix, fmt='%d', delimiter=' ')