import numpy as np

def consecutive_elements(lis):
	lis = np.array(lis)
	lis.sort()
	diffs = np.diff(lis,n=1)
	diffs[diffs > 1] = 0
	return(diffs)

if __name__ == '__main__':
	lis = [100, 4, 200, 1, 3, 2]
	length = consecutive_elements(lis)
	print(length)