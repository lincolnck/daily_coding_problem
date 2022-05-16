import numpy as np

def next(input_array):
	np_input_array = np.asarray(input_array, dtype=object)
	it = np.nditer(np_input_array, flags=['f_index'])
	for x in it:
		print("%d <%d>" % (x, it.index), end=' ') 

test = [[1,2],[3],[],[4,5,6]]
next(test)