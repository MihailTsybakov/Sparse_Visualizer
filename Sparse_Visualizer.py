import matplotlib.pyplot as plt

def print_matrix(matrix : list):
    for row in matrix:
        print(row)

def read_CSR(filename: str):
    matrix = []
    
    input_file = open(filename, 'r')
    txt_data = input_file.read()
    
    parse_tokens = txt_data.split('\n')
    
    N_NNZ = (parse_tokens[0]).split(' ')
    
    N = int(N_NNZ[0])
    NonZero = int(N_NNZ[1])
    
    rows = list(map(lambda elem: int(elem), parse_tokens[1 : N + 2] ))
    cols = list(map(lambda elem: int(elem), parse_tokens[N + 2 : N + 2 + NonZero]))
    elements = list(map(lambda elem: float(elem), parse_tokens[N + 2 + NonZero : N + 3 + 2*NonZero]))
    
    elems_read = 0
    
    for r in range(N):
        
        tmp_row = [0 for i in range(N)]
        elems_in_row = rows[r + 1] - rows[r]
        
        columns = cols[ elems_read : elems_read + elems_in_row ]
        
        for i in range(len(columns)):
            tmp_row[columns[i]] = elements[elems_read + i]
            
        elems_read += elems_in_row
        matrix.append(tmp_row)
    
    return matrix
    
    
matrix_1 = 'Sparse_Matrix_1.txt'

Matrix = read_CSR('Sparse_Matrix_3.txt')

#Plotting
plt.spy(Matrix)