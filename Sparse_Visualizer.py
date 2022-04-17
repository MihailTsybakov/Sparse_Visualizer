import matplotlib.pyplot as plt
from scipy.sparse import csr_array

def print_matrix(matrix : list):
    for row in matrix:
        print(row)

# Returns full matrix as 2D float64 array
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

# Returns bool matrix: True at [x,y] if [x,y]-element != 0, else False
def read_CSR_bool(filename : str):
    matrix = []
    
    input_file = open(filename, 'r')
    txt_data = input_file.read()
    
    parse_tokens = txt_data.split('\n')
    
    N_NNZ = (parse_tokens[0]).split(' ')
    
    N = int(N_NNZ[0])
    NonZero = int(N_NNZ[1])
    
    rows = list(map(lambda elem: int(elem), parse_tokens[1 : N + 2] ))
    cols = list(map(lambda elem: int(elem), parse_tokens[N + 2 : N + 2 + NonZero]))
    elements_bool = list(map(lambda elem: True if float(elem) != 0 else False, parse_tokens[N + 2 + NonZero : N + 3 + 2*NonZero]))
    
    elems_read = 0
    
    for r in range(N):
        
        tmp_row = [False for i in range(N)]
        elems_in_row = rows[r + 1] - rows[r]
        
        columns = cols[ elems_read : elems_read + elems_in_row ]
        
        for i in range(len(columns)):
            tmp_row[columns[i]] = elements_bool[elems_read + i]
            
        elems_read += elems_in_row
        matrix.append(tmp_row)
    
    input_file.close()
    return matrix    
    
# Returns tuple with pure CSR representation
def read_CSR_components(filename : str):
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
    
    input_file.close()
    return (elements, rows, cols, N)
       

data, row_ind, col_ind, N = read_CSR_components('Sparse_Matrix_1.txt')

scipy_CSR = csr_array((data, col_ind, row_ind), shape = (N,N))
plt.spy(scipy_CSR, markersize = 0.01)
plt.savefig('Matrix.png')
