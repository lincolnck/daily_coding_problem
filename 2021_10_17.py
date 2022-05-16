def run_length_encoder(string1):
	for i, v in enumerate(string1):
		while string1[i-1] == v:
			print(v)


if __name__ == '__main__':
	str1 = "AAABBBCCDAA"
	run_length_encoder(str1)