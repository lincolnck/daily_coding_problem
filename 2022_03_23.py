
def cents_to_coins(cents,denominations):
	i = 0
	counter=0
	while cents:
		if cents/denominations[i]<1:
			i+=1
			continue
		cents=cents-denominations[i]
		counter+=1
	return(counter)

if __name__ == '__main__':
	denominations = [25,10,5,1]
	cents = 16
	coins = cents_to_coins(cents,denominations)
	print(coins)