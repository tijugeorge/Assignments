def count_bits(x):
	num_bits = 0
	while x:
		num_bits += x & 1   # any number & 1 will give you result 1 if MSB is 1
							# and we counting that result 1
		x >>= 1				# right shift operator	
	return num_bits

#Driver
print count_bits(13)
