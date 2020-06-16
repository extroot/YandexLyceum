def transpose(matrix):
    st = []
    for i in range(len(matrix[0])):
        s = []
        for x in matrix:
            s.append(x[i])
        st.append(s)
    matrix.clear()
    for x in st:
        matrix.append(x)
