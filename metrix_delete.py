def constructSubmatrix(matrix, rowsToDelete, columnsToDelete):
    new_metrix = []
    for i, j in enumerate(matrix):
        if i not in rowsToDelete:
            row = []
            for n, m in enumerate(j):
                #print n, m
                if n not in columnsToDelete:
                    row.append(m)
            new_metrix.append(row)
    return new_metrix
matrix = [[1, 0, 0, 2],
          [0, 5, 0, 1],
          [0, 0, 3, 5]]

print constructSubmatrix(matrix, [1], [0, 2])