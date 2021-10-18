import numpy as np
import math

def zero_matrix_paths(matrix):
	N, M = matrix.shape[0], matrix.shape[1]
	number = math.factorial(M-1+N-1)/(math.factorial(M-1)*math.factorial(N-1))
	print(number)
	return(number)

if __name__ == '__main__':
	matrix = np.zeros((2,2))
	zero_matrix_paths(matrix)