from fractions import Fraction

def new_frac(fraction):
	numerator = 1
	denominator = 2
	while numerator/denominator > fraction:
		denominator += 1
	new_fraction = fraction-(numerator/denominator)
	added_fraction = numerator/denominator
	return new_fraction, added_fraction;

def egyptian_fraction(fraction):
	new_fraction = fraction
	fracs = []
	sum_of_fracs = 0
	while sum_of_fracs < fraction:
		new_fraction, added_fraction = new_frac(new_fraction)
		fracs.append(added_fraction)
		sum_of_fracs = sum(fracs)
	return fracs

if __name__ == '__main__':
	fracs = egyptian_fraction(4/13)
	print([str(Fraction(item).limit_denominator()) for item in fracs])