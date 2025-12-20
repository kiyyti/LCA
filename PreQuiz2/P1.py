def transpose(a):
    a_transpose = []
    for i in range(len(a[0])):
        at_append = []
        for j in range(len(a)):
            at_append.append(a[j][i])
        a_transpose.append(at_append)
    return a_transpose

