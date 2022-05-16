# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Given a list of integers S and a target number k, write a function that 
# returns a subset of S that adds up to k. If such a subset cannot be made, 
# then return null.

# Integers can appear more than once in the list. You may assume all numbers 
# in the list are positive.

# For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] 
# since it sums up to 24.

def subset_sum(S, target):
	options = [x for x in powerset(S)]
	for x in options:
		if sum(x)==target:
			break
	return x

def powerset(S):
    if len(S) <= 1:
        yield S
        yield []
    else:
        for item in powerset(S[1:]):
            yield [S[0]]+item
            yield item


if __name__ == '__main__':
	S = [12, 1, 61, 5, 9, 2]
	target = 24
	print(subset_sum(S, target))
