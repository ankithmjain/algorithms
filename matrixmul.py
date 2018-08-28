matrices = [1, 2, 3, 3, 4, 2]
def matrixmin(matrices):
    mults = [[]]
    matrix = {i:[matrices[i], matrices[i+1]] for i in range(len(matrices)-1)}
    print matrix
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix)):
            min = 0
            

matrixmin(matrices)