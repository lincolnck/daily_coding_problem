import numpy as np

def count_zero(array):
	zero_els = len(array) - np.count_nonzero(array)
	return zero_els

def edit_distance_roll(string1, string2):
	str1 = np.frombuffer(string1.encode(),'u1')
	str2 = np.frombuffer(string2.encode(),'u1')
	if len(str1)<len(str2):
		str1 = np.pad(str1, (0, (len(str2)-len(str1))),'constant')
	else:
		str2 = np.pad(str2, (0, (len(str1)-len(str2))),'constant')
	counts = []
	count = np.count_nonzero(str1==str2)
	counts.append(count)
	if len(str1)<len(str2):
		for i in len(str2):
			str1test = np.roll(str1, i)
			count = np.count_nonzero(str1test==str2)
			counts.append(count)
	else:
		for i in range(1,len(str1)):
			str2test = np.roll(str2, i)
			count = np.count_nonzero(str1==str2test)
			counts.append(count)

	if len(str1)<len(str2):
		str1test = np.roll(str1, np.argmax(counts))
		print([chr(character) for character in str1test])
		print([chr(character) for character in str2])
		print(count_zero(str1test==str2))
	else:
		str2test = np.roll(str2, np.argmax(counts))
		print([chr(character) for character in str1])
		print([chr(character) for character in str2test])
		print(count_zero(str1==str2test))

def edit_distance(string1, string2):
	str1 = np.frombuffer(string1.encode(),'u1')
	str2 = np.frombuffer(string2.encode(),'u1')
	if len(str1)<len(str2):
		str1 = np.pad(str1, (0, (len(str2)-len(str1))),'constant')
	else:
		str2 = np.pad(str2, (0, (len(str1)-len(str2))),'constant')
	print(count_zero(str1==str2))

if __name__ == "__main__":
	edit_distance("kitten","sitting")