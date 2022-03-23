

def kaprekars_constant(x):
	constant = 6174
	counter=0
	while constant != x:
		forward, reverse = get_sorted_number(x)
		x = reverse - forward
		counter+=1
	return(counter)

def get_sorted_number(n):
    number = str(n)

    number = ''.join(sorted(number))
    reverse_number = ''.join(sorted(number, reverse=True))

    number = int(number)
    reverse_number = int(reverse_number)

    return number, reverse_number
  

if __name__ == '__main__':
	x = 2586
	iterations = kaprekars_constant(x)
	print(iterations)