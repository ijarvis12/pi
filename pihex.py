
print(hex(3)+'.',end='')
max_n = 1000

for n in range(max_n):

	summation = 0.0

	for k in range(n+1):

		nk = 16**(n-k)
        	k1 = 8*k+1
        	k4 = 8*k+4
        	k5 = 8*k+5
        	k6 = 8*k+6
        	
		summation += (
			4*(nk % k1) / k1
			- 2*(nk % k4) / k4
			- (nk % k5) / k5
			- (nk % k6) / k6
		)

	digit = str(summation).split('.')[1]

	digit = hex(round(16*float('0.'+digit)))[-1]

	print(digit,end='',flush=True)

print()
