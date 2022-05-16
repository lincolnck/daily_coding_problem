# The "look and say" sequence is defined as follows: beginning with the term 1, 
# each subsequent term visually describes the digits appearing in the previous 
# term. The first few terms are as follows:

# 1
# 11
# 21
# 1211
# 111221
# As an example, the fourth term is 1211, since the third term 
# consists of one 2 and one 1.

# Given an integer N, print the Nth term of this sequence.

def look_and_say(N):
	n_1 = 1
	for i in range(0,N-1):
		n_n = [int(x) for x in str(n_1)]
		n_nest = split_list(n_n, 0)
		counts = [len(x) for x in n_nest]
		ints = [x[0] for x in n_nest]
		new_num = counts + ints
		new_num[::2]=counts
		new_num[1::2]=ints
		n_1 = int(''.join(str(i) for i in new_num))
	return(n_1)

def split_list(l, n):
    index_list = [i for i in range(1, len(l)) if l[i] - l[i - 1] > n]
    index_list_2 = [i for i in range(1, len(l)) if l[i - 1] - l[i] > n]
    index_list = [None] + sorted(index_list+index_list_2) + [None]
    return [l[index_list[j - 1]:index_list[j]] for j in range(1, len(index_list))]

if __name__ == '__main__':
	N = 6
	nth_term = look_and_say(N)
	print(nth_term)