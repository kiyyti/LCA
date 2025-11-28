# import numpy as np

# def add_mat(f1, f2, outf):
#     matrix1 = np.loadtxt(f1, dtype=int)
#     matrix2 = np.loadtxt(f2, dtype=int)

#     if matrix1.shape != matrix2.shape:
#         open(outf, 'w').close()
#         return
    
#     re_matrix = matrix1 + matrix2
#     np.savetxt(outf, re_matrix, fmt='%d', delimiter=' ')

def readFile(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        mat = []
        for line in f:
            row = list(map(int, line.strip().split()))
            mat.append(row)
    return mat

def add_mat(f1, f2, outf):
    mat1 = readFile(f1)
    mat2 = readFile(f2)
    result = []

    if (len(mat1) != len(mat2)) or (len(f1[0]) != len(f2[0])):
        with open(outf, "w") as f:
            f.write("")
    else:
        for i in range(len(mat1)):
            row = []
            for j in range(len(mat1[0])):
                row.append(mat1[i][j] + mat2[i][j])
            result.append(row)
        with open(outf, "w") as f:
            for i, row in enumerate(result):
                line = " ".join(map(str, row))
                if i != len(result) - 1:
                    line += "\n"
                f.write(line)
if __name__ == '__main__':
    add_mat("mat1.txt","mat2.txt","outmat.txt")
    add_mat("mat1.txt","mat3.txt","outmat1.txt")