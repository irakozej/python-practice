def transpose(lst):

    transposed_mat = []
    rows = len(lst)
    cols = len(lst[0]) if lst else 0

    for i in range(cols):
        transposed_row = []

        for j in range(rows):
            transposed_row.append(lst[j][i])
        transposed_mat.append(transposed_row)
    return transposed_mat


        




        
