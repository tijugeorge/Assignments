def even_odd(A):
	next_even, next_odd = 0, len(A)-1
	while next_even < next_odd:
		if A[next_even]%2==0:
			next_even+=1
		else:
			A[next_even], A[next_odd] = A[next_odd], A[next_even]
			next_odd-=1
	return A




A = [9,8,7,6,5,2,3,1,0]
print A
even_odd(A)
print A
